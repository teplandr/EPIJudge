from collections import Counter

from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    hashtable = Counter(s)
    odd_counter = 0
    for char_count in hashtable.values():
        if char_count & 1:
            odd_counter += 1
    return odd_counter <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
