from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WanderTopo API",
    description="Graph-based travel planning engine API",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Root endpoint for API health check.
    
    Returns:
        dict: Status message indicating API is running
    """
    return {"status": "WanderTopo API is running"}

# Import and include routers
# from .routes import places, recommendations
# app.include_router(places.router)
# app.include_router(recommendations.router) 