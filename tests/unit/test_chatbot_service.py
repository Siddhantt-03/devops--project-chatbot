"""
Unit Tests for DevOps Chatbot Assistant
Student: Siddhant Pandey | 23FE10CSE00011
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src/main'))

from app.services.chatbot_service import (
    get_or_create_session,
    generate_suggested_questions,
    _sessions
)


class TestSessionManagement:
    def test_create_new_session(self):
        sid = get_or_create_session()
        assert sid is not None
        assert isinstance(sid, str)
        assert sid in _sessions

    def test_reuse_existing_session(self):
        sid = get_or_create_session()
        sid2 = get_or_create_session(sid)
        assert sid == sid2

    def test_create_session_with_custom_id(self):
        custom_id = "test-session-123"
        result = get_or_create_session(custom_id)
        assert result == custom_id
        assert custom_id in _sessions


class TestSuggestedQuestions:
    def test_docker_questions(self):
        questions = generate_suggested_questions("How do I use Docker containers?")
        assert len(questions) == 3
        assert any("Docker" in q for q in questions)

    def test_jenkins_questions(self):
        questions = generate_suggested_questions("How do I create a Jenkins pipeline?")
        assert len(questions) == 3
        assert any("Jenkins" in q or "pipeline" in q.lower() for q in questions)

    def test_kubernetes_questions(self):
        questions = generate_suggested_questions("Tell me about Kubernetes pods")
        assert len(questions) == 3
        assert any("Kubernetes" in q for q in questions)

    def test_git_questions(self):
        questions = generate_suggested_questions("What is git branching strategy?")
        assert len(questions) == 3
        assert any("Git" in q or "git" in q for q in questions)

    def test_default_questions(self):
        questions = generate_suggested_questions("How do I become a DevOps engineer?")
        assert len(questions) == 3

    def test_questions_are_strings(self):
        questions = generate_suggested_questions("Docker image")
        for q in questions:
            assert isinstance(q, str)
            assert len(q) > 0
