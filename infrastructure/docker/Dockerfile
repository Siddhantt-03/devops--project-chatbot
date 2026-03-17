# ---- Build Stage ----
FROM python:3.11-slim AS builder

WORKDIR /build

COPY src/main/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --user -r requirements.txt

# ---- Production Stage ----
FROM python:3.11-slim AS production

LABEL maintainer="Siddhant Pandey <23FE10CSE00011>"
LABEL project="DevOps Chatbot Assistant"
LABEL version="1.0.0"

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application source
COPY src/main/ .

# Set ownership
RUN chown -R appuser:appuser /app

USER appuser

ENV PATH=/home/appuser/.local/bin:$PATH
ENV APP_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
