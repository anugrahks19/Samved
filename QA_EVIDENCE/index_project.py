"""Build a local, credential-free file and architecture inventory (not a call graph)."""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json,os,re

ROOT=Path(__file__).resolve().parents[1]
PORTAL='SAMVED_Portal_Updated/JAVA PROJECT OOP'
OUTPUTS={'PROJECT_INDEX.md','PROJECT_INDEX.json'}
SKIP={'.git','.tools','target','node_modules','__pycache__','.roadmap-cache','.venv','venv','dist','build'}
TEXT={'.java','.js','.css','.html','.json','.md','.xml','.yml','.yaml','.properties','.ps1','.cmd','.py','.txt','.toml'}

def link(path,line=None,label=None):
    absolute=(ROOT/path).as_posix()+((':'+str(line)) if line else '')
    return '['+(label or path)+'](<'+absolute+'>)'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--date',default='2026-10-24');args=parser.parse_args()
    entries=[];excluded=[];java=[];routes=[];entities=[];jobs=[]
    for current,dirs,files in os.walk(ROOT,followlinks=False):
        directory=Path(current)
        for name in list(dirs):
            p=directory/name
            if name in SKIP or p.is_symlink():
                excluded.append({'path':p.relative_to(ROOT).as_posix(),'reason':'generated/runtime/VCS/dependency directory or linked directory'});dirs.remove(name)
        dirs.sort()
        for name in sorted(files):
            p=directory/name;rel=p.relative_to(ROOT).as_posix()
            if rel in OUTPUTS:continue
            if name.startswith('.env') and name!='.env.example':
                excluded.append({'path':rel,'reason':'private environment configuration; contents not read'});continue
            if p.is_symlink():
                excluded.append({'path':rel,'reason':'linked file; not followed'});continue
            if rel.startswith(PORTAL+'/'):
                category='active frontend'
                if name in {'script.js','profile.js','portal-nav.js','portal-logout.js'} or '/assets/references/' in rel or p.suffix in {'.md','.lnk'}:category='frontend source artifact excluded from Maven static resources'
            elif rel.startswith('frontend/'):category='retired frontend'
            elif rel.startswith('backend/src/test/'):category='backend tests'
            elif rel.startswith('backend/'):category='backend'
            elif rel.startswith('QA_EVIDENCE/'):category='verification and evidence'
            elif rel.startswith('.agents/'):category='local agent instructions'
            else:category='project documentation, configuration or assets'
            entry={'path':rel,'category':category,'bytes':p.stat().st_size}
            if p.suffix.lower() in TEXT or name=='.gitignore':
                raw=p.read_bytes();text=raw.decode('utf-8-sig',errors='replace');entry['lines']=len(text.splitlines());entry['sha256']=hashlib.sha256(raw).hexdigest()
                if p.suffix=='.java':
                    package=re.search(r'^package\s+([\w.]+);',text,re.M)
                    info={'path':rel,'package':package[1] if package else '',
                        'declarations':[{'kind':m[1],'name':m[2],'line':text.count('\n',0,m.start())+1} for m in re.finditer(r'\b(class|interface|enum|record)\s+(\w+)',text)],
                        'imports':re.findall(r'^import\s+(?:static\s+)?([\w.*]+);',text,re.M)}
                    java.append(info)
                    if '/src/main/' in rel:
                        base=re.search(r'@RequestMapping\(\s*"([^"]+)"',text)
                        for m in re.finditer(r'@(Get|Post|Put|Patch|Delete)Mapping(?:\s*\(([^\n]*?)\))?',text):
                            quoted=re.search(r'"([^"]*)"',m[2] or '')
                            route=(base[1] if base else '')+(quoted[1] if quoted else '')
                            routes.append({'method':m[1].upper(),'path':route,'file':rel,'line':text.count('\n',0,m.start())+1})
                        table=re.search(r'@Table\(\s*name\s*=\s*"([^"]+)"',text)
                        if table:entities.append({'table':table[1],'file':rel,'line':text.count('\n',0,table.start())+1})
                        for m in re.finditer(r'@Scheduled\((.*?)\)',text,re.S):jobs.append({'file':rel,'line':text.count('\n',0,m.start())+1,'configuration':' '.join(m[1].split())})
            entries.append(entry)
    entries.sort(key=lambda e:e['path'])
    pages=json.loads((ROOT/PORTAL/'portal-page-index.json').read_text())
    # The source map stores this page relative to its old feature folder. Keep
    # the runtime map untouched, but index and link to the page's actual path.
    pages={('recommondation page/'+path if path=='progress tracker/index.html' else path):kind
           for path,kind in pages.items()}
    aliases=json.loads((ROOT/PORTAL/'portal-routes.json').read_text())
    snapshot=(ROOT/PORTAL/'backend-visualization/map-data.js').read_text(encoding='utf-8')
    architecture=json.loads(snapshot.removeprefix('window.SAMVED_BACKEND_MAP = ').strip().removesuffix(';'))
    stale=[]
    for feature in architecture['features']:
        for ref in feature['refs']:
            p=ROOT/ref['path'];lines=p.read_text(encoding='utf-8-sig').splitlines()
            if '\n'.join(lines[ref['start']-1:ref['end']])!=ref['code']:stale.append({'feature':feature['id'],'path':ref['path'],'line':ref['start']})
    migrations=sorted(e['path'] for e in entries if re.search(r'/db/migration/V\d+__',e['path']))
    summary={'files':len(entries),'textFiles':sum('lines' in e for e in entries),'mainJavaFiles':sum('/src/main/' in j['path'] for j in java),
        'testJavaFiles':sum('/src/test/' in j['path'] for j in java),'apiMappings':len(routes),'entityTables':len(entities),
        'migrations':len(migrations),'indexedPortalPages':len(pages),'legacyUrlAliases':len(aliases),'scheduledJobs':len(jobs),
        'backendExplorerFeatures':len(architecture['features']),'backendExplorerCodeLocations':sum(len(f['refs']) for f in architecture['features']),
        'staleExplorerReferences':len(stale)}
    report={'indexedOn':args.date,'scope':'all project files except the explicitly listed excluded directories/private configuration; binary assets indexed by metadata only',
        'method':'filesystem inventory and Java annotation/import scanning; no AST call graph or runtime test execution',
        'summary':summary,'categories':dict(Counter(e['category'] for e in entries)),'files':entries,'java':java,
        'apiMappings':routes,'entities':entities,'scheduledJobs':jobs,'migrations':migrations,'pages':pages,'urlAliases':aliases,
        'excluded':excluded,'staleExplorerReferences':stale}
    (ROOT/'PROJECT_INDEX.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    md=['# SAMVED project index','',f'Indexed: {args.date} (Asia/Calcutta). Generated from the current local files.','',
        '## Coverage','',f"{summary['files']} files inventoried; {summary['mainJavaFiles']} main Java files, {summary['testJavaFiles']} test Java files, {len(routes)} API mappings, {len(entities)} entity tables, {len(migrations)} schema migrations, {len(pages)} indexed portal pages and {len(aliases)} legacy URL aliases.",'',
        'This is a file/architecture index, not a semantic call graph. Java declarations, imports, routes, entities and scheduled jobs are scanned from source. Binary assets have metadata only. Credentials, generated builds, runtime caches, dependencies and Git internals are excluded from content indexing. No application tests or external services were run during indexing.','',
        '## Which frontend to edit','',f'**Active:** {link(PORTAL)}. Maven packages this directory into the Java server. **Retired:** `frontend/` is preserved but not used by the current build. Original `script.js`, `profile.js`, `portal-nav.js`, `portal-logout.js`, reference assets, Markdown and shortcut files in the updated portal are excluded by the Maven resource rules.','',
        '## Folder map','', '| Location | Purpose |','| --- | --- |']
    for path,why in [('backend/src/main/java/io/samved','Java application modules, controllers, services and repositories'),('backend/src/main/java/db/migration','Flyway schema migrations'),('backend/src/main/resources','Public application configuration; private .env is excluded'),('backend/src/test','Java/H2 tests and integration checks'),(PORTAL,'Active HTML/CSS/JavaScript pages and assets'),(PORTAL+'/backend-visualization','Public interactive BV architecture explorer'),('frontend','Retired frontend source'),('QA_EVIDENCE','Browser checks, source-map generator, reports and screenshots'),('curation','Opportunity curation data'),('.github/workflows','CI build/test workflow'),('.agents','Local engineering instructions')]:md.append(f'| {link(path)} | {why} |')
    md+=['','## Start, build and verify','',f'- Windows launcher: {link("Start SAMVED.cmd")}; implementation: {link("start-local.ps1")}.',f'- Java 17 / Spring Boot 3.5.16; Maven configuration: {link("backend/pom.xml")}.', '- The same-origin Java server serves frontend and `/api/v1` on port 8080; MySQL defaults to port 3306.', '- Start: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\\start-local.ps1`.', '- Java verification: `mvn -f backend/pom.xml verify`.',f'- Setup: {link("README.md")}, {link("LOCAL_SETUP.md")}, {link("backend/API_CONTRACT.md")}.', '- These are indexed commands, not results of a new build or test run.','',
        '## Backend features and code entry points','', '| Feature | Entry point |','| --- | --- |']
    for f in architecture['features']:
        r=f['refs'][0];md.append(f'| {f["title"]} | {link(r["path"],r["start"],Path(r["path"]).name)} |')
    md+=['','## Main data flow','', 'Login/session → eight-section onboarding gate → saved profile + assessment themes → career candidates / AI estimates + learning-path matches + real opportunities + seven-day action plan → persisted tasks / planner / deadlines → computed progress and reminders.','',
        'Current limitation: AI prompts use onboarding/assessment context; completed-task history is persisted and counted for progress but is not yet fed into adaptive AI planning. Weekly renewal does not by itself implement learning-history adaptation. Journal storage is not implemented.','',
        '## API mappings','', '| Method | Route / route pattern | Code |','| --- | --- | --- |']
    for route in sorted(routes,key=lambda r:(r['path'],r['method'])):md.append(f'| {route["method"]} | `{route["path"].replace("|","&#124;")}` | {link(route["file"],route["line"],Path(route["file"]).name)} |')
    md+=['','## Persistence','', '| Table | Entity |','| --- | --- |']
    for entity in sorted(entities,key=lambda e:e['table']):md.append(f'| `{entity["table"]}` | {link(entity["file"],entity["line"],Path(entity["file"]).name)} |')
    md+=['','### Schema migrations','']+[f'- {link(p)}' for p in migrations]
    md+=['','## Scheduled work','', '| Source | Schedule configuration |','| --- | --- |']
    for job in jobs:md.append(f'| {link(job["file"],job["line"],Path(job["file"]).name)} | `{job["configuration"]}` |')
    md+=['','## Portal pages','', '| Page | Renderer key |','| --- | --- |']
    for path,kind in pages.items():md.append(f'| {link(PORTAL+"/"+path,label=path)} | `{kind}` |')
    md+=['',f'Public additional pages: {link(PORTAL+"/welcome.html")}, {link(PORTAL+"/privacy.html")}, {link(PORTAL+"/backend-visualization/index.html")}.','',
        '## Verification scripts','']+[f'- {link(e["path"])}' for e in entries if e['path'].startswith('QA_EVIDENCE/') and e['path'].endswith('.py')]
    md+=['','## Index maintenance','', '- Rebuild: `python QA_EVIDENCE/index_project.py --date YYYY-MM-DD`.',f'- Complete machine-readable file/declaration/import/route inventory: {link("PROJECT_INDEX.json")}.',f'- Existing BV source references checked against current source: {len(stale)} stale excerpt(s).', '- Generated files, installed tools, nested Git histories and runtime caches are listed in the JSON exclusions, not recursively indexed. Private environment files were not read.','']
    (ROOT/'PROJECT_INDEX.md').write_text('\n'.join(md),encoding='utf-8')
    # Validate the persisted outputs and all extracted paths after writing.
    saved=json.loads((ROOT/'PROJECT_INDEX.json').read_text(encoding='utf-8'))
    assert all((ROOT/e['path']).is_file() for e in saved['files'])
    assert all(not Path(e['path']).name.startswith('.env') or Path(e['path']).name=='.env.example' for e in saved['files'])
    assert len({e['path'] for e in saved['files']})==len(saved['files'])
    assert all((ROOT/PORTAL/path).is_file() for path in saved['pages'])
    assert all(r['path'].startswith('/api/v1') for r in routes)
    print(json.dumps(summary,indent=2));print('VERDICT: PASS - index outputs and source/page paths verified')

if __name__=='__main__':main()
