from typing import List

from test_framework import generic_test


def bsearch(A: List[int], k: int) -> int:
    left, right = 0, len(A) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if A[middle] < k:
            left = middle + 1
        elif A[middle] == k:
            return middle
        else:
            right = middle - 1
    return -1


def search_first_of_k(A: List[int], k: int) -> int:
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        middle = left + (right - left) // 2
        if A[middle] < k:
            left = middle + 1
        elif A[middle] == k:
            result = middle
            right = middle - 1
        else:
            right = middle - 1
    return result

    # index = bsearch(A, k)
    # while index > 0 and A[index - 1] == k:
    #     index -= 1
    # return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
