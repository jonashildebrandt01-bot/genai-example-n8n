# app/main.py

from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI(
    title="Simple FastAPI Example",
    description="A minimal REST API for the n8n project.",
    version="1.0.0"
)

# Example endpoint: GET /hello
@app.get("/hello")
def say_hello(name: str = "World"):
    """
    A simple REST endpoint that returns a greeting.

    Example:
    http://localhost:8000/hello?name=Lisa
    """
    return {"message": f"Hello, {name}!"}


# Root endpoint
@app.get("/")
def root():
    """
    Health-check style endpoint.
    """
    return {"status": "API is running"}
