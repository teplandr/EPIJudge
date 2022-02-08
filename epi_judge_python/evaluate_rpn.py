from test_framework import generic_test


def evaluate(expression: str) -> int:
    OPERATORS = {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x // y
                }
    stack = []
    for token in expression.split(','):
        if token not in OPERATORS:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(OPERATORS[token](a, b))
    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
