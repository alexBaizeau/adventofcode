import re
from collections import Counter

frequencies_dict = {}
all_coordinates = []
claims = {}

with open('day3_1_input.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        matches = re.search('^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$', line)
        claim_number, x, y, width, height = matches.groups()
        line_coordinates = [ (int(x) + dx, int(y) + dy) for dx in range(int(width)) for dy in range(int(height))]
        claims[int(claim_number)] = line_coordinates
        all_coordinates.extend(line_coordinates)
    repeated_coordinates = { coordinate for coordinate, frequency in Counter(all_coordinates).items() if frequency > 1 }

print(f"{len(repeated_coordinates)} is the answer to the first puzzle")

for claim_number, claim_coordinates in claims.items():
    other_coordinates = [ coordinate for index, coordinate_list in claims.items() if index is not claim_number for coordinate in coordinate_list ]
    has_no_overlap = set(other_coordinates).isdisjoint(set(claim_coordinates))
    if has_no_overlap:
        print(f'Claim {claim_number} is the answer to the second puzzle')
