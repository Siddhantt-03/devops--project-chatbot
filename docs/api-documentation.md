# API Documentation — DevOps Chatbot Assistant

**Base URL:** `http://localhost:8000`
**Version:** 1.0.0
**Student:** Siddhant Pandey | 23FE10CSE00011

---

## POST /api/chat

Ask a DevOps question and receive an AI-generated answer.

### Request Body
```json
{
  "message": "string (required, 1-2000 chars)",
  "session_id": "string (optional)"
}
```

### Response
```json
{
  "response": "string",
  "session_id": "string",
  "suggested_questions": ["string", "string", "string"],
  "timestamp": "ISO 8601 datetime"
}
```

### Example
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Docker?"}'
```

```json
{
  "response": "Docker is a platform for developing, shipping, and running applications in containers...",
  "session_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "suggested_questions": [
    "How do I optimize Docker image size?",
    "What is Docker multi-stage build?",
    "How do I use Docker Compose for local development?"
  ],
  "timestamp": "2025-06-15T10:30:00Z"
}
```

---

## GET /health

Returns service health status for monitoring tools.

### Response
```json
{
  "status": "healthy",
  "service": "DevOps Chatbot Assistant",
  "version": "1.0.0",
  "timestamp": "ISO 8601 datetime"
}
```

---

## Error Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 422 | Validation error (empty message, wrong types) |
| 500 | Internal server error (API key missing, AI service down) |
