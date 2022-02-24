import pytest

from generator.services.inn import InnType, generate


@pytest.mark.parametrize("inn_type,inn_len", [
    (InnType.ORGANIZATION, 10),
    (InnType.INDIVIDUAL, 12)
])
def test_generate(inn_type: InnType, inn_len: int):
    result = generate(inn_type)
    assert len(result) == inn_len
