from pydantic import BaseModel

class Crop(BaseModel):
    id: int
    name: str
    focus: str
    soilType: str
    status: str