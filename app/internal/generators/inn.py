import random
import math
from enum import Enum
from typing import Tuple, List

from app.internal.utils.code import add_code_zero_prefix

ORG_INN_N1_CF = (2, 4, 10, 3, 5, 9, 4, 6, 8)
IND_INN_N1_CF = (7,) + ORG_INN_N1_CF
IND_INN_N2_CF = (3, 7,) + ORG_INN_N1_CF


class InnType(str, Enum):
    INDIVIDUAL = 'INDIVIDUAL'
    ORGANIZATION = 'ORGANIZATION'


def generate(inn_type: InnType) -> str:
    region_code = __randomize_code(2)
    ifns_code = __randomize_code(2)
    subject_code = __randomize_code(5 if inn_type == InnType.ORGANIZATION else 6)
    inn_str_part = region_code + ifns_code + subject_code

    if inn_type == InnType.ORGANIZATION:
        n1_check_digit = __calc_organization_check_digit(inn_str_part, ORG_INN_N1_CF)
        return inn_str_part + str(n1_check_digit)

    if inn_type == inn_type.INDIVIDUAL:
        n1_check_digit = __calc_organization_check_digit(inn_str_part, IND_INN_N1_CF)
        n2_check_digit = __calc_organization_check_digit(inn_str_part + str(n1_check_digit), IND_INN_N2_CF)
        return inn_str_part + str(n1_check_digit) + str(n2_check_digit)


def generate_batch(inn_type: InnType, quantity: int) -> List[str]:
    return [generate(inn_type) for _ in range(0, quantity)]


def validate(inn: str) -> bool:
    if len(inn) != 10 and len(inn) != 12:
        return False

    inn_type = InnType.ORGANIZATION if len(inn) == 10 else InnType.INDIVIDUAL

    if inn_type == InnType.ORGANIZATION:
        n1_check_digit = __calc_organization_check_digit(inn[0:9], ORG_INN_N1_CF)
        return inn[-1] == str(n1_check_digit)
    if inn_type == InnType.INDIVIDUAL:
        n1_check_digit = __calc_organization_check_digit(inn[0:10], IND_INN_N1_CF)
        n2_check_digit = __calc_organization_check_digit(inn[0:11], IND_INN_N2_CF)
        return inn[-1] == str(n2_check_digit) and inn[-2] == str(n1_check_digit)


def __calc_organization_check_digit(inn_str: str, table: Tuple[int, ...]) -> int:
    n1_sum = 0

    for i, s in enumerate(inn_str):
        n1_sum += int(s) * table[i]

    remainder = math.ceil(n1_sum % 11)

    return 0 if remainder == 10 else remainder


def __randomize_code(length: int) -> str:
    r_number = random.randint(1, 10 ** length - 1)
    return add_code_zero_prefix(str(r_number), length)

