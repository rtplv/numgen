import pytest

from app.internal.generators.inn import InnType, generate, generate_batch, validate


@pytest.mark.parametrize("inn_type,inn_len", [
    (InnType.ORGANIZATION, 10),
    (InnType.INDIVIDUAL, 12)
])
def test_generate(inn_type: InnType, inn_len: int):
    result = generate(inn_type)
    assert len(result) == inn_len


@pytest.mark.parametrize("inn_type,inn_len", [
    (InnType.ORGANIZATION, 10),
    (InnType.INDIVIDUAL, 12)
])
def test_generate(inn_type: InnType, inn_len: int):
    result = generate(inn_type)
    assert len(result) == inn_len


def test_generate_batch():
    result = generate_batch(InnType.INDIVIDUAL, 50)

    assert len(result) == 50
    assert all([len(r) == 12 for r in result])


def test_validate():
    result = validate("718772591460")
    assert result


def test_validate_invalid():
    result = validate("718772591462")
    assert not result
