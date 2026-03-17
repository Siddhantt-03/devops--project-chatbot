"""
Integration Tests for DevOps Chatbot API
Student: Siddhant Pandey | 23FE10CSE00011
"""

import pytest
import sys
import os
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src/main'))

from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    def test_health_check_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_check_response_body(self):
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "DevOps Chatbot Assistant"
        assert data["version"] == "1.0.0"

    def test_root_endpoint(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "Siddhant Pandey" in data["student"]
        assert "23FE10CSE00011" in data["reg_no"]


class TestChatEndpoint:
    @patch('app.routes.chat.chat')
    def test_chat_returns_200(self, mock_chat):
        mock_chat.return_value = (
            "Here is how to set up Docker...",
            "session-abc-123",
            ["How do I optimize Docker?", "What is Docker Compose?", "What are Docker volumes?"]
        )
        response = client.post("/api/chat", json={"message": "How do I use Docker?"})
        assert response.status_code == 200

    @patch('app.routes.chat.chat')
    def test_chat_response_has_required_fields(self, mock_chat):
        mock_chat.return_value = (
            "CI/CD stands for Continuous Integration and Continuous Deployment...",
            "session-xyz",
            ["What is Jenkins?", "What is GitHub Actions?", "How to set up CI?"]
        )
        response = client.post("/api/chat", json={"message": "What is CI/CD?"})
        data = response.json()
        assert "response" in data
        assert "session_id" in data
        assert "suggested_questions" in data
        assert len(data["suggested_questions"]) > 0

    def test_chat_empty_message_rejected(self):
        response = client.post("/api/chat", json={"message": ""})
        assert response.status_code == 422

    def test_chat_missing_message_rejected(self):
        response = client.post("/api/chat", json={})
        assert response.status_code == 422

    @patch('app.routes.chat.chat')
    def test_chat_with_session_id(self, mock_chat):
        mock_chat.return_value = (
            "Follow-up answer...",
            "existing-session-123",
            ["Q1?", "Q2?", "Q3?"]
        )
        response = client.post("/api/chat", json={
            "message": "Tell me more",
            "session_id": "existing-session-123"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["session_id"] == "existing-session-123"
