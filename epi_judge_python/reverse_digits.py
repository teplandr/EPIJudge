from test_framework import generic_test


def reverse(x: int) -> int:
    result, x_abs = 0, abs(x)
    while x_abs:
        result = result * 10 + x_abs % 10
        x_abs //= 10
    return result if x > 0 else -result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
