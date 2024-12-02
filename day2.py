import sys
from typing import List, Tuple


def is_safe_report(levels):
    # Check if the list has at least 2 numbers
    if len(levels) < 2:
        return False

    # Determine if we're looking for increasing or decreasing based on first pair
    first_diff = int(levels[1]) - int(levels[0])
    if first_diff == 0:  # If first two numbers are equal, it's not safe
        return False

    expecting_increase = first_diff > 0

    # Check each adjacent pair
    for i in range(len(levels) - 1):
        diff = int(levels[i + 1]) - int(levels[i])

        # Check if difference is between 1 and 3 (inclusive)
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        # Check if direction matches what we expect
        if expecting_increase and diff <= 0:
            return False
        if not expecting_increase and diff >= 0:
            return False

    return True


def is_safe_with_dampener(levels):
    # First check if it's safe without dampener
    if is_safe_report(levels):
        return True

    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create new list without the current level
        dampened_levels = levels[:i] + levels[i + 1:]
        if is_safe_report(dampened_levels):
            return True

    return False


def read_input(input_source) -> List[int]:
    list_input = []
    for line in input_source:
        l = line.split(" ")
        list_input.append(l)
    return list_input


def count_safe_reports(list_input):
    # Count safe reports
    safe_count = sum(1 for report in list_input if is_safe_report(report))
    return safe_count


def main():
    """
    Main function to read input, process data, and print results.
    """
    input_source = sys.stdin if len(sys.argv) <= 1 else open(sys.argv[1])
    list_input= read_input(input_source)
    #total_safe_reports = count_safe_reports(list_input)
    safe_count = sum(1 for report in list_input if is_safe_with_dampener(report))
    print(safe_count)
    if input_source is not sys.stdin:
        input_source.close()


if __name__ == "__main__":
    main()