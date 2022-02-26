from app.internal.types.generators import GeneratorType, GeneratorSubType

# В дальнейшем можно это вынести в базу
GENERATOR_TYPES = [
    GeneratorType(
        name="inn",
        label="ИНН",
        subTypes=[
            GeneratorSubType(
                name="individual",
                label="Физ.лицо"
            ),
            GeneratorSubType(
                name="organization",
                label="Организация"
            )
        ]
    )
]