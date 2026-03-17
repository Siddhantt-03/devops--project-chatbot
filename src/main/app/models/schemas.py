"""
Pydantic models for request/response schemas
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ChatMessage(BaseModel):
    role: str = Field(..., description="Role: 'user' or 'assistant'")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, description="User's DevOps question")
    session_id: Optional[str] = Field(None, description="Session ID for conversation continuity")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "How do I set up a Jenkins pipeline for a Python project?",
                "session_id": "abc123"
            }
        }


class ChatResponse(BaseModel):
    response: str = Field(..., description="AI-generated DevOps answer")
    session_id: str = Field(..., description="Session ID for follow-up questions")
    suggested_questions: List[str] = Field(default=[], description="Follow-up questions to explore")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
