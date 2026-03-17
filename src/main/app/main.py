"""
DevOps Chatbot Assistant - Main FastAPI Application
Student: Siddhant Pandey | Reg: 23FE10CSE00011
Course: CSE3253 DevOps [PE6]
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import logging
import time
import os

from app.routes.chat import router as chat_router
from app.routes.health import router as health_router

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="DevOps Chatbot Assistant",
    description=(
        "An AI-powered chatbot that answers DevOps questions, "
        "suggests solutions, and provides best practices for CI/CD, "
        "Docker, Kubernetes, Git, and more."
    ),
    version="1.0.0",
    contact={
        "name": "Siddhant Pandey",
        "email": "23FE10CSE00011@example.edu"
    }
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = round((time.time() - start_time) * 1000, 2)
    logger.info(f"method={request.method} path={request.url.path} status={response.status_code} duration={duration}ms")
    response.headers["X-Process-Time"] = str(duration)
    return response


# Include routers
app.include_router(health_router, tags=["Health"])
app.include_router(chat_router, prefix="/api", tags=["Chat"])

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", tags=["Root"], include_in_schema=False)
async def root():
    index = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(index):
        return FileResponse(index)
    return {
        "message": "DevOps Chatbot Assistant",
        "student": "Siddhant Pandey",
        "reg_no": "23FE10CSE00011",
        "docs": "/docs",
        "health": "/health"
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again later."}
    )
