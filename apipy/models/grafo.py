from pydantic import BaseModel

class Grafo(BaseModel):
    source: str
    target: str
    distance: int