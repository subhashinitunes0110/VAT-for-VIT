from backend.app.models.concept import AnalyzeRequest, ConceptAnalysis


def analyze_concept(request: AnalyzeRequest) -> ConceptAnalysis:
    """
    Perform the first-stage semantic analysis of educational content.

    This is a baseline implementation.
    Later, this service can be replaced or extended with an LLM-based
    semantic analysis pipeline.
    """

    text = request.text.strip()

    return ConceptAnalysis(
        concept=_detect_concept(text),
        domain=_detect_domain(text),
        entities=_extract_entities(text),
        relationships=[],
        steps=[],
        visualization_type=_select_visualization(text),
    )


def _detect_concept(text: str) -> str:
    text_lower = text.lower()

    if "binary search" in text_lower:
        return "Binary Search"

    if "cpu scheduling" in text_lower:
        return "CPU Scheduling"

    if "linked list" in text_lower:
        return "Linked List"

    if "stack" in text_lower:
        return "Stack"

    if "queue" in text_lower:
        return "Queue"

    if "network" in text_lower:
        return "Computer Networks"

    return "Unknown Concept"


def _detect_domain(text: str) -> str:
    text_lower = text.lower()

    if any(
        keyword in text_lower
        for keyword in [
            "binary search",
            "linked list",
            "stack",
            "queue",
            "algorithm",
        ]
    ):
        return "Algorithms and Data Structures"

    if "cpu scheduling" in text_lower:
        return "Operating Systems"

    if "network" in text_lower:
        return "Computer Networks"

    return "Computer Science"


def _extract_entities(text: str) -> list[str]:
    text_lower = text.lower()
    entities = []

    if "binary search" in text_lower:
        entities.extend([
            "sorted array",
            "target",
            "middle element",
        ])

    if "linked list" in text_lower:
        entities.extend([
            "node",
            "data",
            "pointer",
        ])

    if "stack" in text_lower:
        entities.extend([
            "element",
            "top",
        ])

    if "queue" in text_lower:
        entities.extend([
            "element",
            "front",
            "rear",
        ])

    return entities


def _select_visualization(text: str) -> str:
    text_lower = text.lower()

    if "binary search" in text_lower:
        return "algorithm_animation"

    if "linked list" in text_lower:
        return "data_structure_animation"

    if "stack" in text_lower or "queue" in text_lower:
        return "data_structure_animation"

    if "cpu scheduling" in text_lower:
        return "timeline_animation"

    if "network" in text_lower:
        return "network_graph"

    return "concept_diagram"