"""
Healthcare Document Assistant - Main FastAPI Application
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Healthcare Document Assistant",
    description="A GenAI MVP for asking questions over synthetic healthcare documents",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "service": "Healthcare Document Assistant",
        "version": "0.1.0",
    }


@app.get("/")
async def root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to Healthcare Document Assistant",
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
