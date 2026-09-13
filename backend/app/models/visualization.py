from pydantic import BaseModel


class VisualizationData(BaseModel):
    visualization_type: str
    title: str
    entities: list[str] = []
    relationships: list[str] = []
    steps: list[str] = []