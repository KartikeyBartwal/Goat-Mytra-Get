from pydantic import BaseModel, conint, constr, condecimal
from typing import Literal

class GoatClass(BaseModel):
    MilkInLitres: int
    Age: int
    Height: int
    Weight: int
    Pregnancy: int
    Behavior: int
    Gender: str
    HayGrassIntake: int