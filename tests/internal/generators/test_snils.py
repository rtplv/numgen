from app.internal.generators.snils import generate, generate_batch, validate


def test_generate():
    result = generate()
    assert validate(result)


def test_generate_batch():
    result = generate_batch(50)

    assert len(result) == 50


def test_validate():
    result = validate("780 499 002 32")
    assert result


def test_validate_invalid():
    result = validate("780 499 002 31")
    assert not result
