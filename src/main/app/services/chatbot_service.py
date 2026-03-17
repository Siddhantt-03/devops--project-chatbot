"""
Chatbot Service - Core AI logic using Groq API (llama-3.3-70b)
"""

import os
import uuid
import logging
from typing import Dict, List, Tuple
from groq import Groq

logger = logging.getLogger(__name__)

_sessions: Dict[str, List[dict]] = {}

SYSTEM_PROMPT = """You are DevOpsBot, an expert AI assistant specializing in DevOps practices and tools.
You help developers and operations teams with:
- CI/CD pipelines (Jenkins, GitHub Actions, GitLab CI)
- Containerization (Docker, Docker Compose)
- Container orchestration (Kubernetes, Helm)
- Infrastructure as Code (Terraform, Ansible, Puppet)
- Version control (Git, branching strategies)
- Monitoring & logging (Prometheus, Grafana, ELK Stack, Nagios)
- Cloud platforms (AWS, GCP, Azure)
- Security scanning and DevSecOps

Rules:
1. Always provide practical, actionable answers with code examples where relevant.
2. If asked something outside DevOps scope, politely redirect to DevOps topics.
3. Keep answers concise but thorough.
4. Always suggest best practices and potential pitfalls.
5. When providing commands, always include brief explanations.
"""


def get_or_create_session(session_id: str = None) -> str:
    if session_id and session_id in _sessions:
        return session_id
    new_id = session_id or str(uuid.uuid4())
    _sessions[new_id] = []
    return new_id


def generate_suggested_questions(user_message: str) -> List[str]:
    message_lower = user_message.lower()
    if any(kw in message_lower for kw in ["docker", "container", "image"]):
        return ["How do I optimize Docker image size?", "What is Docker multi-stage build?", "How do I use Docker Compose for local development?"]
    elif any(kw in message_lower for kw in ["jenkins", "pipeline", "ci", "cd"]):
        return ["How do I add parallel stages in Jenkins?", "What is the difference between declarative and scripted pipelines?", "How do I trigger Jenkins builds on GitHub push?"]
    elif any(kw in message_lower for kw in ["kubernetes", "k8s", "pod", "deployment"]):
        return ["How do I roll back a Kubernetes deployment?", "What is the difference between Deployment and StatefulSet?", "How do I set up Kubernetes autoscaling?"]
    elif any(kw in message_lower for kw in ["git", "branch", "merge", "commit"]):
        return ["What is GitFlow branching strategy?", "How do I resolve Git merge conflicts?", "What are Git hooks and how to use them?"]
    else:
        return ["What are DevOps best practices for a startup?", "How do I set up a complete CI/CD pipeline?", "What monitoring tools should I use for microservices?"]


def chat(message: str, session_id: str = None) -> Tuple[str, str, List[str]]:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=api_key)
    sid = get_or_create_session(session_id)
    _sessions[sid].append({"role": "user", "content": message})
    history = _sessions[sid][-10:]

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + [
        {"role": msg["role"] if msg["role"] != "assistant" else "assistant", "content": msg["content"]}
        for msg in history
    ]

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
            temperature=0.7,
        )
        assistant_reply = response.choices[0].message.content
        _sessions[sid].append({"role": "assistant", "content": assistant_reply})
        suggested = generate_suggested_questions(message)
        logger.info(f"Chat processed for session={sid}")
        return assistant_reply, sid, suggested

    except Exception as e:
        logger.error(f"Groq API error: {e}")
        _sessions[sid].pop()
        raise
