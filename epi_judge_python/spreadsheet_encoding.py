from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    result = 0
    for c in col:
        result = 26 * result + ord(c) - ord('A') + 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
