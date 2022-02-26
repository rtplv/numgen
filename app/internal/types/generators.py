from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class GeneratorType(str, Enum):
    INN = "INN"


class GenerationSubTypeOption(BaseModel):
    name: str
    label: str


class GenerationTypeOption(BaseModel):
    name: GeneratorType
    label: str
    subTypes: Optional[List[GenerationSubTypeOption]]
