import pytest

from generator.utils.code import add_code_zero_prefix


def test_code():
    result = add_code_zero_prefix("21", 6)
    assert result == "000021"


@pytest.mark.parametrize("code,target_len,expected", [
    ("321523", 2, "321523"),
    ("1000", -10, "1000"),
    ("5632", 0, "5632")
])
def test_code_len(code: str, target_len: int, expected: str):
    result = add_code_zero_prefix(code, target_len)
    assert result == expected


def test_code_empty():
    result = add_code_zero_prefix("", 5)
    assert result == "00000"
