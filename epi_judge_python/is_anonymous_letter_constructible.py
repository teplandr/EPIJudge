from collections import Counter

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_chars = Counter(magazine_text)
    for letter_char in letter_text:
        if letter_char in magazine_chars:
            magazine_chars[letter_char] -= 1
        else:
            return False
    for used_chars in magazine_chars.values():
        if used_chars < 0:
            return False
    return True
    # return not Counter(letter_text) - Counter(magazine_text)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
