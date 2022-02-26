from typing import Optional, List

from pydantic import BaseModel


class GeneratorSubType(BaseModel):
    name: str
    label: str


class GeneratorType(BaseModel):
    name: str
    label: str
    subTypes: Optional[List[GeneratorSubType]]
