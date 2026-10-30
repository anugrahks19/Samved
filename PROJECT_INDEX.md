# SAMVED project index

Indexed: 2026-10-30 (Asia/Calcutta). Generated from the current local files.

## Coverage

447 files inventoried; 86 main Java files, 28 test Java files, 46 API mappings, 11 entity tables, 6 schema migrations, 25 indexed portal pages and 13 legacy URL aliases.

This is a file/architecture index, not a semantic call graph. Java declarations, imports, routes, entities and scheduled jobs are scanned from source. Binary assets have metadata only. Credentials, generated builds, runtime caches, dependencies and Git internals are excluded from content indexing. No application tests or external services were run during indexing.

## Which frontend to edit

**Active:** [SAMVED_Portal_Updated/JAVA PROJECT OOP](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP>). Maven packages this directory into the Java server. **Retired:** `frontend/` is preserved but not used by the current build. Original `script.js`, `profile.js`, `portal-nav.js`, `portal-logout.js`, reference assets, Markdown and shortcut files in the updated portal are excluded by the Maven resource rules.

## Folder map

| Location | Purpose |
| --- | --- |
| [backend/src/main/java/io/samved](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved>) | Java application modules, controllers, services and repositories |
| [backend/src/main/java/db/migration](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration>) | Flyway schema migrations |
| [backend/src/main/resources](<D:/oops 3/oops 2/samved--main/backend/src/main/resources>) | Public application configuration; private .env is excluded |
| [backend/src/test](<D:/oops 3/oops 2/samved--main/backend/src/test>) | Java/H2 tests and integration checks |
| [SAMVED_Portal_Updated/JAVA PROJECT OOP](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP>) | Active HTML/CSS/JavaScript pages and assets |
| [SAMVED_Portal_Updated/JAVA PROJECT OOP/backend-visualization](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/backend-visualization>) | Public interactive BV architecture explorer |
| [frontend](<D:/oops 3/oops 2/samved--main/frontend>) | Retired frontend source |
| [QA_EVIDENCE](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE>) | Browser checks, source-map generator, reports and screenshots |
| [curation](<D:/oops 3/oops 2/samved--main/curation>) | Opportunity curation data |
| [.github/workflows](<D:/oops 3/oops 2/samved--main/.github/workflows>) | CI build/test workflow |
| [.agents](<D:/oops 3/oops 2/samved--main/.agents>) | Local engineering instructions |

## Start, build and verify

- Windows launcher: [Start SAMVED.cmd](<D:/oops 3/oops 2/samved--main/Start SAMVED.cmd>); implementation: [start-local.ps1](<D:/oops 3/oops 2/samved--main/start-local.ps1>).
- Java 17 / Spring Boot 3.5.16; Maven configuration: [backend/pom.xml](<D:/oops 3/oops 2/samved--main/backend/pom.xml>).
- The same-origin Java server serves frontend and `/api/v1` on port 8080; MySQL defaults to port 3306.
- Start: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\start-local.ps1`.
- Java verification: `mvn -f backend/pom.xml verify`.
- Setup: [README.md](<D:/oops 3/oops 2/samved--main/README.md>), [LOCAL_SETUP.md](<D:/oops 3/oops 2/samved--main/LOCAL_SETUP.md>), [backend/API_CONTRACT.md](<D:/oops 3/oops 2/samved--main/backend/API_CONTRACT.md>).
- These are indexed commands, not results of a new build or test run.

## Backend features and code entry points

| Feature | Entry point |
| --- | --- |
| Student interface | [portal-app.js](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/portal-app.js:223>) |
| Identity & security | [WebSecurity.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/config/WebSecurity.java:14>) |
| Onboarding gate | [PersonalRoadmapService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapService.java:51>) |
| Profile & academics | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:15>) |
| Assessment themes | [AssessmentCatalog.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/assessment/AssessmentCatalog.java:12>) |
| Career match & AI | [RecommendationService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/recommendation/RecommendationService.java:81>) |
| AI daily action plan | [ActionPlanService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/ActionPlanService.java:31>) |
| Opportunity matching | [OpportunityMatcher.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/opportunity/OpportunityMatcher.java:14>) |
| Learning roadmaps | [PersonalRoadmapService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapService.java:89>) |
| Daily tasks | [LearningTaskService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTaskService.java:31>) |
| Planner & deadlines | [portal-app.js](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/portal-app.js:211>) |
| Progress & charts | [ProgressController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/progress/ProgressController.java:28>) |
| Deadline reminders | [TaskNotificationService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/notification/TaskNotificationService.java:35>) |
| MySQL & persistence | [pom.xml](<D:/oops 3/oops 2/samved--main/backend/pom.xml:13>) |
| External services | [AiRecommendationService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/recommendation/AiRecommendationService.java:29>) |
| Background jobs | [ActionPlanScheduling.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/ActionPlanScheduling.java:8>) |
| Privacy & cleanup | [DeveloperADataDeletion.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/common/DeveloperADataDeletion.java:14>) |

## Main data flow

Login/session → eight-section onboarding gate → saved profile + assessment themes → career candidates / AI estimates + learning-path matches + real opportunities + seven-day action plan → persisted tasks / planner / deadlines → computed progress and reminders.

Current limitation: AI prompts use onboarding/assessment context; completed-task history is persisted and counted for progress but is not yet fed into adaptive AI planning. Weekly renewal does not by itself implement learning-history adaptation. Journal storage is not implemented.

## API mappings

| Method | Route / route pattern | Code |
| --- | --- | --- |
| POST | `/api/v1/action-plan/ensure` | [ActionPlanController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/ActionPlanController.java:8>) |
| GET | `/api/v1/assessments/current` | [AssessmentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/assessment/AssessmentController.java:18>) |
| PUT | `/api/v1/assessments/current/responses` | [AssessmentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/assessment/AssessmentController.java:23>) |
| GET | `/api/v1/assessments/current/result` | [AssessmentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/assessment/AssessmentController.java:28>) |
| GET | `/api/v1/auth/csrf` | [AuthController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/AuthController.java:30>) |
| POST | `/api/v1/auth/login` | [AuthController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/AuthController.java:35>) |
| POST | `/api/v1/auth/logout` | [AuthController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/AuthController.java:53>) |
| GET | `/api/v1/auth/me` | [AuthController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/AuthController.java:52>) |
| PUT | `/api/v1/auth/password` | [AuthController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/AuthController.java:55>) |
| POST | `/api/v1/auth/register` | [AuthController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/AuthController.java:31>) |
| GET | `/api/v1/careers` | [CareerController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/career/CareerController.java:18>) |
| GET | `/api/v1/careers/{id}` | [CareerController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/career/CareerController.java:23>) |
| PATCH | `/api/v1/milestones/{id}/status` | [RoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapController.java:41>) |
| GET | `/api/v1/notifications` | [TaskNotificationController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/notification/TaskNotificationController.java:15>) |
| PATCH | `/api/v1/notifications/{id}/read` | [TaskNotificationController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/notification/TaskNotificationController.java:16>) |
| GET | `/api/v1/opportunities` | [OpportunityController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/opportunity/OpportunityController.java:30>) |
| GET | `/api/v1/progress/me` | [ProgressController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/progress/ProgressController.java:28>) |
| GET | `/api/v1/recommendations/me` | [RecommendationController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/recommendation/RecommendationController.java:38>) |
| POST | `/api/v1/roadmaps` | [RoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapController.java:36>) |
| GET | `/api/v1/roadmaps/catalogue` | [RoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapController.java:20>) |
| GET | `/api/v1/roadmaps/content` | [RoadmapContentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapContentController.java:10>) |
| GET | `/api/v1/roadmaps/content/guide` | [RoadmapContentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapContentController.java:12>) |
| GET | `/api/v1/roadmaps/content/topic` | [RoadmapContentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapContentController.java:11>) |
| GET | `/api/v1/roadmaps/discover` | [RoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapController.java:24>) |
| GET | `/api/v1/roadmaps/for-role` | [RoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapController.java:30>) |
| GET | `/api/v1/roadmaps/guidance` | [PersonalRoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapController.java:11>) |
| GET | `/api/v1/roadmaps/me` | [RoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapController.java:33>) |
| POST | `/api/v1/roadmaps/preferences` | [PersonalRoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapController.java:12>) |
| PUT | `/api/v1/roadmaps/preferences/active` | [PersonalRoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapController.java:13>) |
| DELETE | `/api/v1/roadmaps/preferences/{slug}` | [PersonalRoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapController.java:14>) |
| DELETE | `/api/v1/students/me` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:22>) |
| GET | `/api/v1/students/me` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:19>) |
| PUT | `/api/v1/students/me` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:20>) |
| GET | `/api/v1/students/me/academics` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:28>) |
| PUT | `/api/v1/students/me/academics` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:29>) |
| GET | `/api/v1/students/me/onboarding` | [PersonalRoadmapController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/PersonalRoadmapController.java:10>) |
| PUT | `/api/v1/students/me/review/{section}` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:21>) |
| GET | `/api/v1/students/me/skills` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:26>) |
| PUT | `/api/v1/students/me/skills` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:27>) |
| GET | `/api/v1/students/me/{section:interests&#124;strengths&#124;values}` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:24>) |
| PUT | `/api/v1/students/me/{section:interests&#124;strengths&#124;values}` | [StudentController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentController.java:25>) |
| GET | `/api/v1/tasks` | [LearningTaskController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTaskController.java:12>) |
| POST | `/api/v1/tasks` | [LearningTaskController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTaskController.java:13>) |
| DELETE | `/api/v1/tasks/{id}` | [LearningTaskController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTaskController.java:18>) |
| PUT | `/api/v1/tasks/{id}` | [LearningTaskController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTaskController.java:14>) |
| PATCH | `/api/v1/tasks/{id}/status` | [LearningTaskController.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTaskController.java:16>) |

## Persistence

| Table | Entity |
| --- | --- |
| `assessment_responses` | [AssessmentResponse.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/assessment/AssessmentResponse.java:15>) |
| `careers` | [Career.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/career/Career.java:17>) |
| `learning_tasks` | [LearningTask.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/LearningTask.java:8>) |
| `opportunities` | [Opportunity.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/opportunity/Opportunity.java:9>) |
| `roadmap_catalogue_entries` | [RoadmapCatalogueEntry.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapCatalogueEntry.java:10>) |
| `roadmap_milestones` | [RoadmapMilestone.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/RoadmapMilestone.java:7>) |
| `roadmaps` | [Roadmap.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/roadmap/Roadmap.java:8>) |
| `student_action_plans` | [StudentActionPlan.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/StudentActionPlan.java:6>) |
| `student_profiles` | [StudentProfile.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/student/StudentProfile.java:8>) |
| `task_notifications` | [TaskNotification.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/notification/TaskNotification.java:18>) |
| `users` | [Account.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/auth/Account.java:8>) |

### Schema migrations

- [backend/src/main/java/db/migration/V1__developer_a_schema.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration/V1__developer_a_schema.java>)
- [backend/src/main/java/db/migration/V2__task_notifications.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration/V2__task_notifications.java>)
- [backend/src/main/java/db/migration/V3__roadmap_catalogue_cache.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration/V3__roadmap_catalogue_cache.java>)
- [backend/src/main/java/db/migration/V4__accounts_and_profiles.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration/V4__accounts_and_profiles.java>)
- [backend/src/main/java/db/migration/V5__guidance_preferences.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration/V5__guidance_preferences.java>)
- [backend/src/main/java/db/migration/V6__automatic_action_plans.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/db/migration/V6__automatic_action_plans.java>)

## Scheduled work

| Source | Schedule configuration |
| --- | --- |
| [TaskNotificationService.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/notification/TaskNotificationService.java:34>) | `fixedDelayString = "${samved.reminders.poll-ms:3600000}"` |
| [OpportunityFeedRefresh.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/opportunity/OpportunityFeedRefresh.java:28>) | `fixedDelayString = "${samved.opportunity.refresh-ms:21600000}", initialDelayString = "${samved.opportunity.initial-delay-ms:15000}"` |
| [UnstopOpportunityRefresh.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/opportunity/UnstopOpportunityRefresh.java:55>) | `fixedDelayString = "${samved.unstop.refresh-ms:21600000}", initialDelayString = "${samved.unstop.initial-delay-ms:30000}"` |
| [ActionPlanScheduling.java](<D:/oops 3/oops 2/samved--main/backend/src/main/java/io/samved/task/ActionPlanScheduling.java:9>) | `cron="0 10 0 * * *",zone="Asia/Kolkata"` |

## Portal pages

| Page | Renderer key |
| --- | --- |
| [login.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/login.html>) | `login` |
| [register.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/register.html>) | `register` |
| [academic-details/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/academic-details/index.html>) | `academic-details` |
| [activities/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/activities/index.html>) | `activities` |
| [assessment/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/assessment/index.html>) | `assessment` |
| [career roadmap/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/career roadmap/index.html>) | `career roadmap` |
| [charts/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/charts/index.html>) | `charts` |
| [daily tasks/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/daily tasks/index.html>) | `daily tasks` |
| [dashboard/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/dashboard/index.html>) | `dashboard` |
| [deadline system/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/deadline system/index.html>) | `deadline system` |
| [form assessment/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/form assessment/index.html>) | `form assessment` |
| [interests/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/interests/index.html>) | `interests` |
| [journal/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/journal/index.html>) | `journal` |
| [oppertunity page/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/oppertunity page/index.html>) | `oppertunity page` |
| [planner/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/planner/index.html>) | `planner` |
| [profile/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/profile/index.html>) | `profile` |
| [profile completion/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/profile completion/index.html>) | `profile completion` |
| [recommondation page/progress tracker/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/recommondation page/progress tracker/index.html>) | `progress tracker` |
| [recommondation page/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/recommondation page/index.html>) | `recommondation page` |
| [skills/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/skills/index.html>) | `skills` |
| [strengths/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/strengths/index.html>) | `strengths` |
| [values/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/values/index.html>) | `values` |
| [career-goal/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/career-goal/index.html>) | `career-goal` |
| [onboarding/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/onboarding/index.html>) | `onboarding` |
| [onboarding/prepare.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/onboarding/prepare.html>) | `preparation` |

Public additional pages: [SAMVED_Portal_Updated/JAVA PROJECT OOP/welcome.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/welcome.html>), [SAMVED_Portal_Updated/JAVA PROJECT OOP/privacy.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/privacy.html>), [SAMVED_Portal_Updated/JAVA PROJECT OOP/backend-visualization/index.html](<D:/oops 3/oops 2/samved--main/SAMVED_Portal_Updated/JAVA PROJECT OOP/backend-visualization/index.html>).

## Verification scripts

- [QA_EVIDENCE/action_plan_live.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/action_plan_live.py>)
- [QA_EVIDENCE/backend_explorer_check.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/backend_explorer_check.py>)
- [QA_EVIDENCE/build_backend_map.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/build_backend_map.py>)
- [QA_EVIDENCE/index_project.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/index_project.py>)
- [QA_EVIDENCE/onboarding_flow_check.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/onboarding_flow_check.py>)
- [QA_EVIDENCE/onboarding_live.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/onboarding_live.py>)
- [QA_EVIDENCE/ui_error_states.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/ui_error_states.py>)
- [QA_EVIDENCE/ui_interactions.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/ui_interactions.py>)
- [QA_EVIDENCE/ui_layout_check.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/ui_layout_check.py>)
- [QA_EVIDENCE/ui_smoke.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/ui_smoke.py>)
- [QA_EVIDENCE/updated_portal_check.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/updated_portal_check.py>)
- [QA_EVIDENCE/updated_portal_live.py](<D:/oops 3/oops 2/samved--main/QA_EVIDENCE/updated_portal_live.py>)

## Index maintenance

- Rebuild: `python QA_EVIDENCE/index_project.py --date YYYY-MM-DD`.
- Complete machine-readable file/declaration/import/route inventory: [PROJECT_INDEX.json](<D:/oops 3/oops 2/samved--main/PROJECT_INDEX.json>).
- Existing BV source references checked against current source: 0 stale excerpt(s).
- Generated files, installed tools, nested Git histories and runtime caches are listed in the JSON exclusions, not recursively indexed. Private environment files were not read.
