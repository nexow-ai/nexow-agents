"""FastAPI application for nexow-agents service."""

from fastapi import FastAPI
import structlog

from nexow_agents.config import settings

logger = structlog.get_logger(__name__)

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
