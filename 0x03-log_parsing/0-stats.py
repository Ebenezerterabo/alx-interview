#!/usr/bin/python3
import re
import sys


def read_line(line):
    """
    Parses a line of input and returns the status code and file size.
    """
    pattern = r'''
    ^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.)
    {3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\s-\s
    \[\]\s"GET /projects/\d+ HTTP/1.1"\s(\d{3})\s(\d+)$
    '''

    # Check if the patterns matches the pattern
    match = re.match(pattern, line.strip())
    # If the line matches extract the status code and file size
    if match:
        status_code = match.group(3)
        file_size = int(match.group(4))
        return status_code, file_size

    # If the line doesn't match, return None
    return None


def collect_data(status_code, file_size, stats):
    """
    Updates the statistics dictionary with the given status code
    and file size
    """
    # Update the total file size
    stats['total_file_size'] += file_size
    # Update the count for the status code
    if status_code in stats['status_codes']:
        stats['status_codes'][status_code] += 1
    else:
        stats['status_codes'][status_code] = 1


def display_statistics(statistics):
    """
    Prints the total file size and the number of lines for each status code
    and file size.

    Args:
        statics (dict): The dictionary holding the statistics.
    """

    # Print the total file size
    print(f"File size: {statistics['total_file_size']}")
    # Print the number of lines for each status code in ascending order
    for code in sorted(statistics['status_codes']):
        print(f"{code}: {statistics['status_codes'][code]}")


def main():
    # Initialize statistics dictionary
    statistics = {
        'total_file_size': 0,
        'status_codes': {}
    }

    line_count = 0
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break  # Exit the loop if no more input

            result = read_line(line)
            if result is not None:
                status_code, file_size = result
                collect_data(status_code, file_size, statistics)
                line_count += 1

            if line_count == 10:
                display_statistics(statistics)
                line_count = 0  # Reset after printing statistics
        except KeyboardInterrupt:
            display_statistics(statistics)
            break


if __name__ == "__main__":
    main()
