from fastapi import FastAPI

app = FastAPI(
    title="Adaptive Visual Learning Assistant",
    description="Source-grounded adaptive knowledge-to-visualization system",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Adaptive Visual Learning Assistant API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }