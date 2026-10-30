# SAMVED frontend

The active website is served by the Java Spring Boot application on http://127.0.0.1:8080. Maven copies this folder into the app. Restart/rebuild after editing pages. A standalone static server does not provide the API.

The served pages now use the visual system from `SAMVED_Portal_Updated/JAVA PROJECT OOP/`: `portal-pages.css` is copied from that folder, its illustrations are under `assets/illustrations/`, and `portal-shell.js` builds its header, sidebar, main card, and right rail around the API-backed pages. `auth/auth-shell.js` uses the updated artwork around the working login and registration forms. The prototype's sample data, browser-only saves, and mock alerts are not used as account behavior.

Registration, login and logout use server sessions. Profile pages save personal details, academic records/subjects, interests, skills, strengths, values and career goals to MySQL. Passwords are hashed on the server and are never stored in browser storage. Previous prototype accounts must be registered again.

All private feature pages use api/developer-a-api.js for requests and api/session.js to load the signed-in account. The profile sections share profile/profile-sections.js. Account settings provide password change and permanent account deletion. Analytics reads actual saved records rather than demonstration arrays.

Assessment, recommendations, roadmap milestones, tasks, progress, opportunities and reminders use the existing Java endpoints under /api/v1. AI and external catalogues depend on the server provider configuration; empty opportunity feeds are shown honestly.

See ../LOCAL_SETUP.md for the double-click launcher, prerequisites and configuration. See auth/privacy.html for the local pilot notice.
