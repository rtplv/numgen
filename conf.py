from app.internal.generators.inn import InnType
from app.internal.types.generators import GenerationTypeOption, GenerationSubTypeOption, GeneratorType

# В дальнейшем можно это вынести в базу
GENERATOR_TYPES = [
    GenerationTypeOption(
        name=GeneratorType.INN,
        label="ИНН",
        subTypes=[
            GenerationSubTypeOption(
                name=InnType.INDIVIDUAL.value,
                label="Физ.лицо"
            ),
            GenerationSubTypeOption(
                name=InnType.ORGANIZATION.value,
                label="Организация"
            )
        ]
    )
]