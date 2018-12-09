import re
from collections import Counter

frequencies_dict = {}
coordinates = []
with open('day3_1_input.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        matches = re.search('^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$', line)
        index, x, y, width, height = matches.groups()
        line_coordinates = [ (int(x) + dx, int(y) + dy) for dx in range(int(width)) for dy in range(int(height))]
        coordinates.extend(line_coordinates)
    repeated_coordinates = { coordinate for coordinate, frequency in Counter(coordinates).items() if frequency > 1 }

print(f"{len(repeated_coordinates)} is the answer")
