import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    result = []
    for i in range(size):
        if s[i] == 'a':
            result.extend(['d', 'd'])
        elif s[i] == 'b':
            continue
        else:
            result.append(s[i])
    for i in range(len(result)):
        s[i] = result[i]
    return len(result)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
