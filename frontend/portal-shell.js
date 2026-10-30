/* SAMVED_Portal_Updated layout around the existing server-backed pages. */
(() => {
  const groups = [
    ['Journey',
      ['⌂', 'Home', '/dashboard/index.html'],
      ['👤', 'Profile', '/profile/profile.html'],
      ['🎓', 'Academic details', '/profile/academic.html'],
      ['♡', 'Interests', '/profile/interests.html'],
      ['⚙', 'Skills', '/profile/skills.html'],
      ['⭐', 'Strengths', '/profile/strengths.html'],
      ['💎', 'Values', '/profile/values.html'],
      ['🎯', 'Career goal', '/profile/careergoal.html'],
      ['📋', 'Assessment', '/assessment/assessment.html']],
    ['Explore and track',
      ['🗺', 'Career roadmap', '/career%20roadmap/index.html'],
      ['📈', 'Progress', '/progress%20tracker/index.html'],
      ['📝', 'Daily tasks', '/daily%20tasks/index.html'],
      ['⏳', 'Deadlines', '/deadline%20system/index.html'],
      ['🌟', 'Opportunities', '/oppertunity%20page/index.html'],
      ['💡', 'Recommendations', '/recommondation%20page/index.html'],
      ['📊', 'Charts', '/charts/index.html']]
  ];
  const illustrations = [
    [/academic/, 'STUDY_GIRL.jpeg', 'Your academic journey'],
    [/interests/, 'INTERSET.jpeg', 'Explore your interests'],
    [/skills/, 'SKILL.jpeg', 'Grow your skills'],
    [/strengths/, 'STRENGTH.jpeg', 'Build on your strengths'],
    [/values/, 'VALUES.jpeg', 'Your values'],
    [/assessment/, 'ASSESMENT.jpeg', 'Career assessment'],
    [/progress|charts/, 'PROGRESS.jpeg', 'Your progress'],
    [/daily|deadline/, 'ACTIVITIES.jpeg', 'Plan your activities'],
    [/profile/, 'WELCOME.jpeg', 'Your career profile']
  ];
  function node(tag, className, value) {
    const item = document.createElement(tag);
    if (className) item.className = className;
    if (value) item.textContent = value;
    return item;
  }
  function build() {
    const content = document.querySelector('.portal-layout') || document.querySelector('.main-wrapper');
    if (!content) return;
    document.body.classList.add('samved-themed');
    content.classList.add('samved-content-root');
    const shell = node('div', 'app-layout samved-portal-adapter');
    const top = node('header', 'portal-topbar');
    const menu = node('button', 'samved-menu-toggle', '☰');
    menu.type = 'button';
    menu.setAttribute('aria-label', 'Open navigation');
    menu.setAttribute('aria-expanded', 'false');
    menu.addEventListener('click', () => {
      const open = document.body.classList.toggle('samved-nav-open');
      menu.setAttribute('aria-expanded', String(open));
      menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    top.appendChild(menu);
    const brand = node('a', 'portal-brand');
    brand.href = '/dashboard/index.html';
    const logo = node('img', 'portal-brand-logo');
    logo.src = '/assets/samved-portal-logo.png';
    logo.alt = 'SAMVED Portal';
    brand.appendChild(logo);
    top.appendChild(brand);
    const search = node('form', 'portal-search-wrap');
    search.setAttribute('role', 'search');
    const searchIcon = node('span', 'portal-search-icon', '⌕');
    searchIcon.setAttribute('aria-hidden', 'true');
    const searchInput = node('input', 'portal-search-input');
    searchInput.type = 'search';
    searchInput.placeholder = 'Search pages, skills, roadmaps…';
    searchInput.setAttribute('aria-label', 'Find a SAMVED page');
    search.append(searchIcon, searchInput);
    search.addEventListener('submit', event => {
      event.preventDefault();
      const query = searchInput.value.trim().toLowerCase();
      if (!query) return;
      const links = groups.flatMap(([, ...entries]) => entries);
      const match = links.find(([, label]) => label.toLowerCase() === query)
        || links.find(([, label]) => label.toLowerCase().includes(query));
      if (match) location.assign(match[2]);
      else {
        searchInput.setCustomValidity('No matching page. Try profile, tasks, skills, or roadmaps.');
        searchInput.reportValidity();
      }
    });
    searchInput.addEventListener('input', () => searchInput.setCustomValidity(''));
    top.appendChild(search);
    const actions = node('div', 'portal-header-actions');
    const reminders = node('a', 'portal-notif-btn', '🔔');
    reminders.href = '/dashboard/index.html#notifications-container';
    reminders.setAttribute('aria-label', 'View reminders');
    const profile = node('a', 'portal-user-profile');
    profile.href = '/profile/profile.html';
    profile.title = 'View profile';
    const avatar = node('span', 'samved-avatar', 'S');
    avatar.setAttribute('aria-label', 'Signed in student');
    profile.append(avatar, node('span', 'portal-user-chevron', '▼'));
    actions.append(reminders, profile);
    top.appendChild(actions);
    const grid = node('div', 'portal-body-grid');
    const sidebar = node('aside', 'portal-sidebar');
    const nav = node('nav');
    nav.setAttribute('aria-label', 'Main navigation');
    const current = decodeURIComponent(location.pathname).toLowerCase();
    for (const [heading, ...links] of groups) {
      nav.appendChild(node('div', 'samved-nav-group', heading));
      const list = node('ul', 'portal-nav-list');
      for (const [icon, label, path] of links) {
        const item = node('li', 'portal-nav-item');
        const link = node('a', 'portal-nav-link');
        link.href = path;
        const resolved = decodeURIComponent(new URL(path, location.href).pathname).toLowerCase();
        if (resolved === current) {
          item.classList.add('active');
          link.classList.add('active');
          link.setAttribute('aria-current', 'page');
        }
        link.append(node('span', 'portal-nav-icon', icon), document.createTextNode(label));
        item.appendChild(link);
        list.appendChild(item);
      }
      nav.appendChild(list);
    }
    sidebar.appendChild(nav);
    const footer = node('div', 'portal-sidebar-footer');
    const signout = node('button', 'portal-sidebar-btn logout', '🚪  Sign out');
    signout.type = 'button';
    signout.addEventListener('click', () => window.logout && window.logout());
    const quote = node('div', 'portal-footer-quote', 'Small steps build big dreams ♡');
    footer.append(signout, quote);
    sidebar.appendChild(footer);
    const center = node('div', 'portal-main-card samved-main-card');
    center.appendChild(content);
    const rail = node('aside', 'portal-right-rail');
    rail.setAttribute('aria-label', 'Helpful information');
    const image = illustrations.find(([pattern]) => pattern.test(current))
      || [/./, 'WELCOME.jpeg', 'Your career journey'];
    const art = node('div', 'portal-ill-card');
    const picture = node('img', 'portal-ill-img contain');
    picture.src = `/assets/illustrations/${image[1]}`;
    picture.alt = image[2];
    art.appendChild(picture);
    rail.appendChild(art);
    const info = node('div', 'portal-info-card');
    info.appendChild(node('h2', 'portal-info-card-title', 'Your saved journey'));
    info.appendChild(node('p', 'portal-info-card-text', 'Your profile, assessment, roadmaps and tasks are saved to your SAMVED account.'));
    const infoLink = node('a', 'portal-info-card-link', 'View my profile →');
    infoLink.href = '/profile/profile.html';
    info.appendChild(infoLink);
    rail.appendChild(info);
    grid.append(sidebar, center, rail);
    shell.append(top, grid);
    document.body.prepend(shell);
    if (window.SamvedSession) window.SamvedSession.then(account => {
      if (account && account.name) {
        avatar.textContent = account.name.charAt(0).toUpperCase();
        avatar.setAttribute('aria-label', account.name);
      }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build, {once: true});
  else build();
})();
