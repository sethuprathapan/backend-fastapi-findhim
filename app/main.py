from fastapi import FastAPI

app = FastAPI(
    title="Task Management API",
    description="REST API for managing tasks with role-based access control.",
    version="1.0.0",
)


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "Okay", "message": "Task Management API is running."}
