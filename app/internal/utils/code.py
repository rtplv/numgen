def add_code_zero_prefix(code: str, target_len: int):
    result_code = code
    for _ in range(target_len - len(str(code))):
        result_code = "0" + result_code
    return result_code
