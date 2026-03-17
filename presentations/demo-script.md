# Demo Script — DevOps Chatbot Assistant
**Student:** Siddhant Pandey | 23FE10CSE00011
**Duration:** 5-7 minutes

---

## [0:00 - 0:30] Introduction
"Hi, I'm Siddhant Pandey, registration number 23FE10CSE00011. My project is a DevOps Chatbot Assistant — an AI-powered chatbot that answers DevOps questions and suggests solutions. It's built with Python FastAPI and uses the Anthropic Claude AI API."

---

## [0:30 - 1:30] Project Structure Walkthrough
- Show the repository folder structure
- Highlight: `src/main/app/`, `infrastructure/docker/`, `infrastructure/kubernetes/`, `pipelines/`, `tests/`

---

## [1:30 - 3:00] Live Demo — Running the App
```bash
# Start with Docker Compose
docker-compose -f infrastructure/docker/docker-compose.yml up --build
```
- Open browser at http://localhost:8000/docs
- Show Swagger UI
- Execute POST /api/chat with: "How do I create a Jenkins pipeline?"
- Show the AI response and suggested_questions
- Ask a follow-up using the returned session_id

---

## [3:00 - 4:00] CI/CD Pipeline Demo
- Open Jenkins / GitHub Actions
- Show pipeline stages: Lint → Build → Test → Security Scan → Deploy
- Show passing status

---

## [4:00 - 5:00] Docker & Kubernetes
```bash
docker images | grep devops-chatbot
kubectl get pods,svc,deploy
```
- Show running pods
- Show LoadBalancer service

---

## [5:00 - 5:30] Monitoring
- Open Nagios at http://localhost:8081
- Show health check passing for devops-chatbot

---

## [5:30 - 6:00] Closing
"This project demonstrates a complete DevOps lifecycle — from AI-powered application development to containerization, CI/CD, Kubernetes orchestration, and monitoring. Thank you."
