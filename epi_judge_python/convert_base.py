from test_framework import generic_test


def toint(c: str) -> int:
    if c.isdigit():
        return ord(c) - ord('0')
    if c.isalpha():
        return ord(c) - ord('A') + 10


def tostr(i: int) -> str:
    return chr(ord('0') + i) if i < 10 else chr(ord('A') + i - 10)


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    base10 = 0

    is_negative = num_as_string[0] == '-'

    for c in num_as_string[is_negative:]:
        base10 = base10 * b1 + toint(c)

    s = []
    while True:
        s += tostr(base10 % b2)
        base10 //= b2
        if base10 == 0:
            break

    if is_negative:
        s += '-'

    return ''.join(reversed(s))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
