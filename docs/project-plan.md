# Project Plan & Timeline

**Project:** DevOps Chatbot Assistant
**Student:** Siddhant Pandey | 23FE10CSE00011
**Course:** CSE3253 DevOps [PE6] | Semester VI (2025-2026)

---

## Project Timeline

| Week | Phase | Tasks | Status |
|------|-------|-------|--------|
| 1 | Planning | Requirements, design, tech stack selection | ✅ Done |
| 2 | Core Dev | FastAPI app, Google Gemini API integration | ✅ Done |
| 3 | DevOps Setup | Docker, Docker Compose, CI/CD pipeline | ✅ Done |
| 4 | Kubernetes | Deployment manifests, service, configmap | ✅ Done |
| 5 | Testing | Unit tests, integration tests, coverage | ✅ Done |
| 6 | Monitoring | Nagios config, health checks, alerts | ✅ Done |
| 7 | Documentation | README, API docs, user guide | ✅ Done |
| 8 | Demo & Submit | Demo video, final review, submission | 🔄 In Progress |

---

## Milestones

1. **M1 - Working Chatbot API** — FastAPI + Claude API responding to DevOps questions
2. **M2 - Containerized App** — Docker image built and running via docker-compose
3. **M3 - CI/CD Pipeline** — Jenkins + GitHub Actions pipeline passing all stages
4. **M4 - Kubernetes Ready** — Deployment manifests applied and pods running
5. **M5 - Monitored** — Nagios health checks active and alerting configured
6. **M6 - Fully Documented** — All docs complete, demo video recorded

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Google Gemini API rate limits | Medium | High | Implement retry logic and caching |
| Docker image size too large | Low | Medium | Multi-stage build with slim base image |
| Kubernetes cluster unavailable | Low | High | Fallback to Docker Compose deployment |
| Test coverage below 80% | Medium | Medium | Write tests alongside feature development |
