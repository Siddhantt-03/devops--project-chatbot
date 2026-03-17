"""
Chat API Routes
"""

from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import chat
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/chat", response_model=ChatResponse, summary="Ask a DevOps question")
async def chat_endpoint(request: ChatRequest):
    """
    Send a DevOps-related question to the AI chatbot.

    - **message**: Your DevOps question (max 2000 characters)
    - **session_id**: Optional. Pass the session_id from a previous response to continue conversation.

    Returns an AI-generated answer with follow-up question suggestions.
    """
    try:
        response_text, session_id, suggested = chat(
            message=request.message,
            session_id=request.session_id
        )
        return ChatResponse(
            response=response_text,
            session_id=session_id,
            suggested_questions=suggested
        )
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        logger.error(f"Chat endpoint error: {e}")
        raise HTTPException(status_code=500, detail="Failed to process your request.")
