import re
from math import inf
from collections import Counter

puzzle_input = []

def manhattan_distance(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


with open('day6.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        x, y = re.search('(\d+),\s(\d+)', line).groups()
        x = int(x)
        y = int(y)
        puzzle_input.append((x, y))

x_min = puzzle_input[0][0]
x_max = x_min
y_min = puzzle_input[0][1]
y_max = y_min

for x, y in puzzle_input:
    if x < x_min:
        x_min = x
    if x > x_max:
        x_max = x

    if y < y_min:
        y_min = y
    if y > y_max:
        y_max = y
max_distance = 10000
closest_coordinate_indices = []
coordinates_within_max_region = []
for dx in range(x_min, x_max+1):
    for dy in range(y_min, y_max+1):
        min_distance = inf
        min_index = 0
        total_distance = 0

        tile_distances = []
        for index, vector in enumerate(puzzle_input):
            distance = manhattan_distance(vector, (dx, dy))
            total_distance = total_distance + distance
            tile_distances.append((index, distance))
        # sort distances - if two (index, distance) tuple has the same distance
        # Then that tile is close to two coordiantes and does not count, otherwise
        # claim that tile for the index
        tile_distances.sort(key=lambda tup: tup[1])
        if (tile_distances[0][1] < tile_distances[1][1]):
            closest_coordinate_indices.append(tile_distances[0][0])

        if total_distance < max_distance:
            coordinates_within_max_region.append((dx, dy))

areas_without_infinites = [index for index in closest_coordinate_indices
                            if puzzle_input[index][0] not in [x_min, x_max]
                                and puzzle_input[index][0] not in [y_min, y_max]]

largest_area = Counter(areas_without_infinites).most_common(1)[0][1]
print(f'The largest area is {largest_area}')
print(f'The answer of puzzle 2 is {len(coordinates_within_max_region)}')
