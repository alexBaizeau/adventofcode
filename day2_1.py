from collections import Counter
from functools import reduce

frequencies_dict = {}
with open('day2_1_input.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        count = Counter(line).most_common()
        frequencies = { frequency for _, frequency in count }
        for frequency in frequencies:
            if frequency < 2:
                continue
            frequencies_dict[frequency] = frequencies_dict.get(frequency, 0) + 1

hashed_result = reduce(lambda x,y: x*y, [total for _, total in frequencies_dict.items()])
print(f'{hashed_result} is the answer')
