from backend.app.models.concept import ConceptAnalysis
from backend.app.models.visualization import VisualizationData


def create_visualization_data(
    analysis: ConceptAnalysis,
) -> VisualizationData:
    """
    Convert semantic analysis into visualization-ready data.
    """

    return VisualizationData(
        visualization_type=analysis.visualization_type or "concept_diagram",
        title=analysis.concept,
        entities=analysis.entities,
        relationships=analysis.relationships,
        steps=analysis.steps,
    )