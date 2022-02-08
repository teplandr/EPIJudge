from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack, brackets = [], {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in brackets:
            stack.append(c)
        elif not stack or brackets[stack.pop()] != c:
            return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
