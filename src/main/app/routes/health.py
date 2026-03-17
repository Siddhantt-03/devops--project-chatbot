"""
Health Check Route
"""

from fastapi import APIRouter
from app.models.schemas import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, summary="Health check")
async def health_check():
    """Returns service health status. Used by monitoring tools like Nagios."""
    return HealthResponse(
        status="healthy",
        service="DevOps Chatbot Assistant",
        version="1.0.0"
    )
