from backend.app.models.concept import AnalyzeRequest, ConceptAnalysis


def analyze_concept(request: AnalyzeRequest) -> ConceptAnalysis:
    """
    Perform the first-stage semantic analysis of educational content.

    This baseline implementation identifies:
    - concept
    - domain
    - entities
    - relationships
    - procedural steps
    - suitable visualization type

    The rule-based implementation can later be extended with
    an LLM-based semantic analysis pipeline.
    """

    text = request.text.strip()

    concept = _detect_concept(text)

    return ConceptAnalysis(
        concept=concept,
        domain=_detect_domain(text),
        entities=_extract_entities(text),
        relationships=_extract_relationships(text, concept),
        steps=_extract_steps(text, concept),
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

    if "cpu scheduling" in text_lower:
        return "Operating Systems"

    if "network" in text_lower:
        return "Computer Networks"

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

    return "Computer Science"


def _extract_entities(text: str) -> list[str]:
    text_lower = text.lower()
    entities = []

    if "binary search" in text_lower:
        entities.extend([
            "sorted array",
            "target",
            "middle element",
            "left boundary",
            "right boundary",
        ])

    if "linked list" in text_lower:
        entities.extend([
            "node",
            "data",
            "pointer",
            "head",
            "next node",
        ])

    if "stack" in text_lower:
        entities.extend([
            "element",
            "top",
            "push",
            "pop",
        ])

    if "queue" in text_lower:
        entities.extend([
            "element",
            "front",
            "rear",
            "enqueue",
            "dequeue",
        ])

    if "cpu scheduling" in text_lower:
        entities.extend([
            "process",
            "CPU",
            "burst time",
            "waiting time",
            "turnaround time",
        ])

    if "network" in text_lower:
        entities.extend([
            "node",
            "router",
            "packet",
            "connection",
        ])

    return _remove_duplicates(entities)


def _extract_relationships(text: str, concept: str) -> list[str]:
    """
    Identify the important relationships between entities.

    Relationships are currently represented as readable strings.
    Later, these can be converted into structured graph edges.
    """

    text_lower = text.lower()

    if concept == "Binary Search":
        return [
            "sorted array contains target",
            "middle element is compared with target",
            "comparison determines search half",
            "left boundary and right boundary define search range",
        ]

    if concept == "Linked List":
        return [
            "node contains data",
            "node points to next node",
            "head points to first node",
            "nodes form a sequential structure",
        ]

    if concept == "Stack":
        return [
            "top identifies the active end of the stack",
            "push adds an element to the top",
            "pop removes an element from the top",
            "stack follows LIFO order",
        ]

    if concept == "Queue":
        return [
            "front identifies the removal end",
            "rear identifies the insertion end",
            "enqueue adds an element at the rear",
            "dequeue removes an element from the front",
            "queue follows FIFO order",
        ]

    if concept == "CPU Scheduling":
        return [
            "CPU executes processes",
            "scheduling algorithm determines process order",
            "process order affects waiting time",
            "process order affects turnaround time",
        ]

    if concept == "Computer Networks":
        return [
            "nodes communicate through connections",
            "routers forward packets",
            "packets travel between network nodes",
        ]

    return []


def _extract_steps(text: str, concept: str) -> list[str]:
    """
    Extract the conceptual/procedural steps required for visualization.
    """

    if concept == "Binary Search":
        return [
            "Start with the sorted array",
            "Identify the middle element",
            "Compare the middle element with the target",
            "If the target is smaller, search the left half",
            "If the target is larger, search the right half",
            "Repeat until the target is found or the search range is empty",
        ]

    if concept == "Linked List":
        return [
            "Start at the head node",
            "Read the current node's data",
            "Follow the pointer to the next node",
            "Repeat until the required node is reached or the list ends",
        ]

    if concept == "Stack":
        return [
            "Identify the top of the stack",
            "Push adds an element to the top",
            "Pop removes the top element",
            "Continue operations while maintaining LIFO order",
        ]

    if concept == "Queue":
        return [
            "Identify the front and rear",
            "Enqueue adds an element at the rear",
            "Dequeue removes an element from the front",
            "Continue operations while maintaining FIFO order",
        ]

    if concept == "CPU Scheduling":
        return [
            "Identify the available processes",
            "Apply the scheduling policy",
            "Select the next process",
            "Execute the selected process",
            "Update scheduling metrics",
        ]

    if concept == "Computer Networks":
        return [
            "Identify communicating network nodes",
            "Create or identify the network connection",
            "Send packets through the network",
            "Forward packets through intermediate nodes",
            "Deliver packets to the destination",
        ]

    return []


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


def _remove_duplicates(items: list[str]) -> list[str]:
    """
    Preserve insertion order while removing duplicate entities.
    """

    return list(dict.fromkeys(items))