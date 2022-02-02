from test_framework import generic_test


def reverse_bits(x: int) -> int:
    result = 0
    for i in range(64):
        b = bool(x & (1 << i))
        result |= b << (63 - i)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
