# User Guide — DevOps Chatbot Assistant

**Student:** Siddhant Pandey | 23FE10CSE00011

---

## Getting Started

### 1. Start the Application
```bash
# With Docker (recommended)
docker-compose -f infrastructure/docker/docker-compose.yml up --build

# Without Docker
cd src/main
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. Open the API
Navigate to **http://localhost:8000/docs** to open the interactive Swagger UI.

---

## Using the Chatbot

### Ask a Question (curl)
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "How do I create a Jenkins pipeline?"}'
```

### Continue a Conversation (curl)
```bash
# Use the session_id returned from the first response
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Can you show me a Jenkinsfile example?", "session_id": "YOUR_SESSION_ID"}'
```

### Sample Questions to Try
- "How do I write a multi-stage Dockerfile?"
- "What is the difference between Docker and Kubernetes?"
- "Explain the GitFlow branching strategy"
- "How do I set up Prometheus monitoring?"
- "What are best practices for CI/CD pipelines?"

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info |
| GET | `/health` | Health check |
| POST | `/api/chat` | Ask a DevOps question |
| GET | `/docs` | Swagger UI |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `500 - GEMINI_API_KEY not set` | Add your API key to `.env` file |
| Container won't start | Run `docker-compose logs chatbot` to see errors |
| Slow responses | Normal for first request; AI model warm-up takes ~1-2s |
| Empty response | Ensure your question is at least 1 character |
