# Technical Design Document

**Project:** DevOps Chatbot Assistant
**Student:** Siddhant Pandey | 23FE10CSE00011
**Version:** 1.0.0

---

## 1. Architecture Overview

The application follows a layered REST API architecture:

```
Client (Browser / Postman / curl)
        ↓  HTTP
  FastAPI Application (Port 8000)
        ↓
  Chatbot Service Layer
        ↓
  Google Gemini API (gemini-1.5-flash)
```

---

## 2. Component Breakdown

### 2.1 API Layer (FastAPI)
- **Framework:** FastAPI 0.111
- **Routes:** `/health`, `/api/chat`, `/` (root), `/docs` (Swagger)
- **Middleware:** CORS, request logging, global exception handler
- **Validation:** Pydantic v2 models

### 2.2 Service Layer
- `chatbot_service.py` — Core logic: session management, Google Gemini API calls, suggested question generation
- In-memory session store (dict) with conversation history per session
- Context limited to last 10 messages to control token usage

### 2.3 AI Integration
- Model: `gemini-1.5-flash`
- System prompt enforces DevOps-only scope
- Multi-turn conversation via message history passed on each request

---

## 3. Data Flow

```
1. Client sends POST /api/chat { message, session_id? }
2. ChatRequest validated by Pydantic
3. chatbot_service.chat() called
4. Session retrieved or created
5. User message appended to session history
6. History (last 10 msgs) + system prompt sent to Google Gemini API
7. AI response received and appended to session
8. ChatResponse returned { response, session_id, suggested_questions }
```

---

## 4. Deployment Architecture

```
┌─────────────────────────────────────────────────┐
│  Kubernetes Cluster                             │
│  ┌───────────────────┐  ┌───────────────────┐  │
│  │  Pod 1            │  │  Pod 2            │  │
│  │  devops-chatbot   │  │  devops-chatbot   │  │
│  │  :8000            │  │  :8000            │  │
│  └───────────────────┘  └───────────────────┘  │
│           ↑                       ↑             │
│  ┌─────────────────────────────────────────┐   │
│  │  LoadBalancer Service (port 80)         │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
            ↑
        Internet
```

---

## 5. Security Design

- API key stored in Kubernetes Secret / `.env` file (never hardcoded)
- Non-root Docker user (`appuser`)
- Pydantic input validation on all endpoints
- CORS configured (restrict in production)
- Security headers via FastAPI middleware

---

## 6. Technology Justification

| Technology | Reason |
|-----------|--------|
| FastAPI | High performance, async support, auto Swagger docs |
| Google Gemini | Best-in-class language model for technical Q&A |
| Docker | Consistent environments, easy deployment |
| Kubernetes | Production-grade orchestration, auto-scaling |
| GitHub Actions | Native CI/CD integration with GitHub |
| Nagios | Industry-standard monitoring, proven reliability |
