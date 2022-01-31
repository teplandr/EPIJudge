from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    tmp = []
    x_abs = abs(x)
    while x_abs:
        tmp += chr(ord('0') + x_abs % 10)
        x_abs //= 10

    if x < 0:
        tmp += '-'

    return ''.join(reversed(tmp))


def string_to_int(s: str) -> int:
    result = 0
    start = 1 if s[0] == '+' or s[0] == '-' else 0
    for c in s[start:]:
        result = result * 10 + (ord(c) - ord('0'))
    return -result if s[0] == '-' else result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))