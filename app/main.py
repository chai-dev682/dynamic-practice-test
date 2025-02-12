from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import test
from app.core.config import settings

app = FastAPI(
    title="Dynamic Practice Test API",
    description="API for generating adaptive practice test questions",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    # In production, replace with specific origins
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(test.router, prefix="/api/v1/test", tags=["test"])

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"} 