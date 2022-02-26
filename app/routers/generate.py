from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.internal.generators.inn import InnType, generate_batch
from app.internal.types.generators import GenerationTypeOption, GeneratorType
from conf import GENERATOR_TYPES

router = APIRouter(
    prefix="/generate",
    tags=["generate"],
)


class GenerateBody(BaseModel):
    quantity: int = Field(ge=1, le=100)
    type: GeneratorType
    subtype: str


@router.post("/")
def generate(body: GenerateBody) -> List[str]:
    if body.type == GeneratorType.INN:
        try:
            subtype = InnType(body.subtype)
        except ValueError:
            raise HTTPException(
                status_code=403,
                detail=f"subtype {body.subtype} is invalid. Must be in: {[t.value for t in InnType]}"
            )

        return generate_batch(subtype, body.quantity)

    return []


@router.get("/types")
def get_types() -> List[GenerationTypeOption]:
    return GENERATOR_TYPES


