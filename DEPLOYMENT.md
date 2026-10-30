# Public deployment (Render)

SAMVED is a Java 17 Spring Boot application that serves both the active portal pages and `/api/v1` from one origin. Deploy the repository root as one Render Docker web service. This preserves the existing session-cookie and CSRF setup.

## Before you deploy

1. Push this project to a GitHub repository.
2. Create a reachable MySQL 8 database with a database and app user. Render does not provide managed MySQL; use a managed MySQL provider or a separately operated MySQL server. Enable TLS for the database connection when the provider supports it, and allow the Render service to connect.
3. Save the database host, port, database name, username, and password. Do not add production credentials to GitHub.

## Deploy on Render

1. In Render, choose **New + → Blueprint**, connect the GitHub repository, and select its branch. Render reads `render.yaml` and builds the repository's `Dockerfile`.
2. For the `samved` web service, enter the three prompted environment values:
   - `SAMVED_DB_URL`: `jdbc:mysql://<database-host>:<port>/<database-name>?sslMode=REQUIRED` (use the exact TLS options required by your MySQL provider).
   - `SAMVED_DB_USER`: the MySQL app username.
   - `SAMVED_DB_PASSWORD`: the MySQL app password.
3. Deploy. Wait for `/actuator/health` to pass, then open the `onrender.com` URL shown in the service dashboard and go to `/login.html`.
4. Register a new account and complete onboarding. The application runs Flyway migrations at startup; the configured database user needs permission to create and update tables.

The app reads Render's `PORT` setting, enables secure session cookies for HTTPS, and packages `SAMVED_Portal_Updated/JAVA PROJECT OOP` into its Java server. The free web-service plan can sleep when idle, so the first request after inactivity may take a little time to start.

## Optional AI integration

To enable the optional NVIDIA-backed recommendations and roadmap generation, add `SAMVED_NVIDIA_API_KEY` as a secret environment variable in the Render dashboard. Keep it out of the repository. The site remains usable without that optional key, using its built-in fallback behavior.

## Deployment shape

```text
Browser → Render Java/Spring Boot service → external MySQL 8
                      ├─ active portal pages
                      └─ /api/v1 backend
```

Vercel is not required for this setup. It can serve static frontend files, but Java still needs a backend host; splitting the app also adds a proxy requirement to preserve same-origin sessions and CSRF. For a first public project URL, Render hosting the combined app is the simpler fit.
