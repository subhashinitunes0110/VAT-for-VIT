from fastapi import FastAPI

from backend.app.models.concept import AnalyzeRequest, ConceptAnalysis
from backend.app.models.visualization import VisualizationData

from backend.app.services.semantic_analyzer import analyze_concept
from backend.app.services.visualization_service import create_visualization_data


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


@app.post("/analyze", response_model=ConceptAnalysis)
def analyze(request: AnalyzeRequest):
    return analyze_concept(request)


@app.post("/visualize", response_model=VisualizationData)
def visualize(request: AnalyzeRequest):
    analysis = analyze_concept(request)

    return create_visualization_data(analysis)