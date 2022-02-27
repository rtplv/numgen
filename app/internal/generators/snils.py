import random
from typing import List
from app.internal.utils.code import add_code_zero_prefix


def generate() -> str:
    num_parts = [__generate_part() for i in range(3)]

    # Wiki: Проверка контрольного числа Страхового номера проводится только для номеров больше номера 001-001-998
    if num_parts[0] == 1 and num_parts[1] == 1 and num_parts[3] < 999:
        return __concat_num_parts(num_parts)

    return f"{__concat_num_parts(num_parts)} {__get_check_digit(num_parts)}"


def generate_batch(quantity: int) -> List[str]:
    return [generate() for _ in range(0, quantity)]


def validate(inn: str) -> bool:
    pass


def __generate_part() -> int:
    return random.randint(1, 999)


def __concat_num_parts(parts: List[int]):
    num_str = ' '.join(map(lambda p: add_code_zero_prefix(str(p), 3), parts))
    return num_str


def __get_check_digit(num_parts: List[int]):
    multiply_sum = 0
    num_parts_str = ''.join(map(lambda p: add_code_zero_prefix(str(p), 3), num_parts))

    for pos in range(9, 0, -1):
        num = int(num_parts_str[-pos])
        multiply_sum += num * pos

    return __calc_check_digit_from_sum(multiply_sum)


def __calc_check_digit_from_sum(multiply_sum: int):
    if multiply_sum < 100:
        return str(multiply_sum)
    if multiply_sum == 100 or multiply_sum == 101:
        return "00"
    if multiply_sum > 101:
        remainder = multiply_sum % 101
        return __calc_check_digit_from_sum(remainder)


a = generate()