import sys
from typing import List, Tuple


def read_input(input_source) -> Tuple[List[int], List[int]]:
    """
    Reads input from the given source and returns two lists of integers.

    Args:
        input_source: The source to read input from (file or stdin).

    Returns:
        A tuple containing two lists of integers.
    """
    left, right = [], []
    for line in input_source:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    return left, right


def calculate_totals(left: List[int], right: List[int]) -> Tuple[int, int]:
    """
    Calculates the totals for the given lists.

    Args:
        left: A list of integers.
        right: A list of integers.

    Returns:
        A tuple containing two totals.
    """
    left.sort()
    right.sort()
    total1 = sum(abs(l - r) for l, r in zip(left, right))
    total2 = sum(l * right.count(l) for l in left)
    return total1, total2


def main():
    """
    Main function to read input, process data, and print results.
    """
    input_source = sys.stdin if len(sys.argv) <= 1 else open(sys.argv[1])
    left, right = read_input(input_source)
    total1, total2 = calculate_totals(left, right)
    print('Part 1:', total1)
    print('Part 2:', total2)
    if input_source is not sys.stdin:
        input_source.close()


if __name__ == "__main__":
    main()