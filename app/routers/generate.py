from typing import List

from fastapi import APIRouter

from app.internal.types.generators import GeneratorType
from conf import GENERATOR_TYPES

router = APIRouter(
    prefix="/generate",
    tags=["generate"],
)


@router.get("/types")
def get_types() -> List[GeneratorType]:
    return GENERATOR_TYPES

