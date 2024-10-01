#!/usr/bin/python3

""" 0-stats module """
import re
import sys


def read_line(line):
    """
    Parses a line of input and returns the status code and file size.
    """
    pattern = r'''
    ^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s   # IP address
    \[(.*?)\]\s                               # Timestamp (non-greedy match)
    "GET\s/[^"]*\sHTTP/1\.1"\s                # Request (constant format)
    (\d{3})\s                                 # Status code
    (\d+)$                                    # File size
    '''

    # Check if the patterns matches the pattern
    match = re.match(pattern, line.strip(), re.VERBOSE)
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
    # stats['status_codes'][status_code]
    # = stats['status_codes'].get(status_code, 0) + 1
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
    """ Main function """
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

            if result:
                status_code, file_size = result
                collect_data(status_code, file_size, statistics)
                line_count += 1

            if line_count == 10:
                display_statistics(statistics)
                line_count = 0  # Reset after printing statistics

        except Exception as e:
            pass
        finally:
            display_statistics(statistics)


if __name__ == "__main__":
    main()
