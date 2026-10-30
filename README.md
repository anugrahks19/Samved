# SAMVED — Student Career Guidance & Opportunity Portal

[![Java](https://img.shields.io/badge/Java-17-orange.svg)](https://www.oracle.com/java/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5.16-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-blue.svg)](https://www.mysql.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7.svg)](https://render.com/)

SAMVED is an end-to-end full-stack career guidance and opportunity discovery platform built with Java 17, Spring Boot, MySQL, and a modern single-origin web frontend. It empowers students to discover career pathways through psychometric assessment, tailored learning roadmaps, AI-driven action plans, and verified opportunity feeds.

🌐 **Live Demo:** [https://samved-u063.onrender.com/login.html](https://samved-u063.onrender.com/login.html)

---

## Key Features

* **Secure Authentication & Account Security:**
  * User registration, BCrypt password hashing, session rotation, CSRF token validation, and IP rate limiting.
  * Same-origin cookie architecture with strict CSRF protection on all state-altering endpoints.

* **Guided 8-Stage Onboarding Flow:**
  * Mandatory baseline setup: Profile Info, Academic History, Interests, Skills & Proficiency, Strengths, Values, and Career Direction.
  * Comprehensive 8-question psychometric career assessment evaluating cognitive and behavioral dimensions.

* **Intelligent Career Matching & Roadmap Generation:**
  * Rule-based scoring with optional **NVIDIA NIM** LLM integration for personalized career matching and custom role roadmaps.
  * Visual interactive milestone explorer with external roadmap resources and progress trackers.

* **Actionable Daily Planner & Deadlines:**
  * Daily learning task manager with due dates, priorities, and status updates (`PENDING`, `IN_PROGRESS`, `COMPLETED`).
  * Automated deadline notification engine providing in-app reminders for upcoming and overdue milestones.

* **Verified Opportunity Discovery:**
  * Curated and categorized repository of internships, hackathons, scholarships, courses, and events.
  * Real-time relevancy matching calculated against student profiles, skills, and goals.

* **Progress & Academic Analytics:**
  * Central dashboard displaying student progress percentages, milestone completions, and skill distributions.

---

## Architecture & Technology Stack

```text
Browser Client (HTML5 / CSS3 / Vanilla JS)
        │
        ▼ (HTTPS / Same-Origin)
Spring Boot Web Application (Java 17)
  ├── Web Security & CSRF Filter
  ├── REST API Controllers (/api/v1)
  │    ├── Auth & Profile Services
  │    ├── Assessment & Recommendation Engine (Optional NVIDIA NIM)
  │    ├── Personal Roadmaps & Action Planner
  │    └── Opportunity Discovery Feeds
  └── Static Resource Server (Serves the compiled portal UI)
        │
        ▼ (TLS JDBC Connection)
Aiven Cloud / Local MySQL 8.0 Database (Flyway Schema Migrations)
```

| Layer | Technologies |
| :--- | :--- |
| **Backend** | Java 17, Spring Boot 3.5.16, Spring Data JPA, Spring Security, Flyway |
| **Database** | MySQL 8.0 (Managed on Aiven Cloud / Local MySQL Server) |
| **Frontend** | Responsive HTML5, CSS3, ES6+ JavaScript (`portal-app.js`) |
| **Containerization & Hosting** | Multi-stage Docker build, Render Cloud Platform |
| **External AI** | NVIDIA NIM API (`gpt-oss-20b`) with robust rule-based fallbacks |

---

## Directory Structure

```text
├── backend/                              # Java 17 / Spring Boot backend application
│   ├── pom.xml                           # Maven project config (bundles frontend into static/)
│   ├── src/main/java/io/samved/          # Modules: auth, student, assessment, roadmap, task, etc.
│   ├── src/main/resources/               # Database properties and configurations
│   └── src/test/                         # Integration and unit test suites
├── SAMVED_Portal_Updated/                # Active frontend web application
│   └── JAVA PROJECT OOP/                 # Production HTML, CSS, assets, and portal-app.js
├── curation/                             # Seed dataset of verified opportunities
├── Dockerfile                            # Production multi-stage Docker container build
├── render.yaml                           # Infrastructure Blueprint for automated Render deployment
├── DEPLOYMENT.md                         # Cloud hosting and environment variable guide
├── Start SAMVED.cmd                      # 1-click Windows local development launcher
└── start-local.ps1                       # PowerShell local launch script
```

---

## Local Setup & Development

### Prerequisites
* **Java Development Kit (JDK) 17+**
* **MySQL Server 8.0+**
* **Apache Maven 3.9+** (or use the included wrapper)

### 1. Database Setup
In MySQL Workbench or the MySQL CLI, create the database:
```sql
CREATE DATABASE IF NOT EXISTS samved CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'samved'@'127.0.0.1' IDENTIFIED BY 'your-password';
GRANT ALL PRIVILEGES ON samved.* TO 'samved'@'127.0.0.1';
```

### 2. Configure Environment
Copy `backend/.env.example` to `backend/.env` and update your database credentials:
```properties
SAMVED_DB_URL=jdbc:mysql://127.0.0.1:3306/samved
SAMVED_DB_USER=samved
SAMVED_DB_PASSWORD=your-password
SAMVED_SECURE_COOKIE=false
```

### 3. Build & Run
**Windows (Quick Start):**
Double-click `Start SAMVED.cmd` or run:
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\start-local.ps1
```

**Manual Maven Build:**
```bash
mvn -f backend/pom.xml clean package -DskipTests
java -jar backend/target/samved-backend-0.1.0-SNAPSHOT.jar
```

Visit **`http://127.0.0.1:8080/login.html`** in your browser.

---

## Cloud Deployment (Render + Managed MySQL)

The repository is pre-configured for automated deployment via Render Blueprints and Docker.

1. Create a MySQL 8 database on a cloud provider such as **[Aiven](https://aiven.io/)** or **[Railway](https://railway.app/)**.
2. Connect your GitHub repository in the **[Render Dashboard](https://dashboard.render.com/)** using **New + → Blueprint**.
3. Supply the environment variables:
   * `SAMVED_DB_URL`: `jdbc:mysql://<host>:<port>/defaultdb?sslMode=REQUIRED`
   * `SAMVED_DB_USER`: `<database-username>`
   * `SAMVED_DB_PASSWORD`: `<database-password>`
   * *(Optional)* `SAMVED_NVIDIA_API_KEY`: `<your-nvidia-key>`
4. Render automatically compiles the container, executes Flyway migrations, and provides a live public HTTPS URL. See [DEPLOYMENT.md](DEPLOYMENT.md) for full instructions.

---

## API Documentation

The complete REST API specification is documented in [backend/API_CONTRACT.md](backend/API_CONTRACT.md).
All endpoints are namespaced under `/api/v1` and enforce session authentication and CSRF token verification.
