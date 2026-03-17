# Self Assessment — DevOps Chatbot Assistant

**Student:** Siddhant Pandey
**Registration No:** 23FE10CSE00011
**Course:** CSE3253 DevOps [PE6]

---

## Marks Breakdown

| Criteria | Max Marks | Self Score | Remarks |
|----------|-----------|------------|---------|
| Implementation | 4 | 4 | Fully working FastAPI chatbot with Anthropic AI integration, multi-turn conversation support, session management |
| Documentation | 3 | 3 | Comprehensive README, API docs, user guide, design document, project plan |
| Innovation | 2 | 2 | AI-powered DevOps assistant with context memory and suggested follow-up questions |
| Presentation | 1 | 1 | Demo script prepared, Swagger UI as live demo, demo video in deliverables |
| **Total** | **10** | **10** | |

---

## Challenges & Solutions

1. **Multi-turn conversation context** — Anthropic API is stateless; solved by maintaining per-session message history in memory and passing the last 10 messages with each request.

2. **Docker image size** — Initial image was 1.2GB; reduced to ~180MB using multi-stage builds with `python:3.11-slim` and copying only installed packages.

3. **Keeping AI on-topic** — Without guardrails the model would answer non-DevOps questions; solved with a focused system prompt that restricts responses to DevOps scope.

---

## Learnings

- How to build production-grade REST APIs with FastAPI including middleware, error handling, and Swagger docs
- Integrating external AI APIs into real-world applications with proper error handling and session management
- End-to-end DevOps pipeline: code → Docker → CI/CD → Kubernetes → monitoring
- Importance of multi-stage Docker builds for production-ready images
- How Kubernetes rolling updates and health probes work in practice
