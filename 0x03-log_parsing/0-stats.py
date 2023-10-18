#!/usr/bin/python3
""" module with stats fn """

import sys

count = 0
stats = {}
file_size = 0

try:
    for line in sys.stdin:
        count += 1
        data = line.split()
        code, f_size = data[-2], int(data[-1])
        # store status codes -> count in dict & add file_size
        if not stats.get(code):
            stats[code] = 1
        else:
            stats[code] += 1  # count for number of spec status codes
        file_size += f_size

        if count % 10 == 0:
            # print the stats
            print(f"File size: {file_size}")
            for key in sorted(stats.keys()):
                print(f"{key}: {stats[key]}")
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {file_size}")
    for key in sorted(stats.keys()):
        print(f"{key}: {stats[key]}")
