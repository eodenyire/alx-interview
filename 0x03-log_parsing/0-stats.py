#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Initialize metrics
total_file_size = 0
status_counts = defaultdict(int)
line_count = 0

# Define valid status codes
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Define a regex pattern to match the expected log format
log_pattern = re.compile(
        r"^(\S+) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$")


def print_stats():
    """Prints the current statistics for file size and status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)

        # Process only if the line matches the expected format
        if match:
            ip_address, date, status_code, file_size = match.groups()
            file_size = int(file_size)
            total_file_size += file_size
            if status_code in valid_status_codes:
                status_counts[status_code] += 1
            line_count += 1

        # Print stats every 10 lines
        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    pass

finally:
    # Print final statistics upon interruption or end of input
    print_stats()
