from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Educational content to analyze"
    )


class ConceptAnalysis(BaseModel):
    concept: str
    domain: str | None = None
    entities: list[str] = []
    relationships: list[str] = []
    steps: list[str] = []
    visualization_type: str | None = None