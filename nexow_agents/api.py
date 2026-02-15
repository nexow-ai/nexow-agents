"""FastAPI application for nexow-agents service."""

from fastapi import FastAPI
from pydantic_settings import BaseSettings
import structlog

logger = structlog.get_logger(__name__)


class Settings(BaseSettings):
    """Application settings."""
    port: int = 8002
    environment: str = "development"
    
    # LLM API Keys
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    tavily_api_key: str = ""


settings = Settings()

app = FastAPI(
    title="Nexow Agents Service",
    description="Agent management - AI reasoning and strategy templates",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "nexow-agents"}


@app.get("/status")
async def get_status():
    """Get service status."""
    return {
        "service": "nexow-agents",
        "version": "0.1.0",
        "environment": settings.environment,
    }


# TODO: Add agent CRUD endpoints
# - POST /agents - Create agent
# - GET /agents - List agents
# - GET /agents/{id} - Get agent
# - PUT /agents/{id} - Update agent
# - DELETE /agents/{id} - Delete agent
# - POST /agents/{id}/execute - Execute agent strategy
