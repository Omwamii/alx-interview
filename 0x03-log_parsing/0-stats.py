#!/usr/bin/python3
""" module with stats fn """
import sys

stats = {}
file_size, count = 0, 0

try:
    for line in sys.stdin:
        data = line.split()

        if len(data) < 2:
            continue
        count += 1
        code, f_size = data[-2], int(data[-1])

        # store status codes -> count in dict & add file_size
        try:
            code = int(code)
        except ValueError:
            pass
        else:
            if not stats.get(code):
                stats[code] = 1
            else:
                stats[code] += 1  # count for number of spec status codes
        finally:
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
