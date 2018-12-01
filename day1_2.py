import urllib.request
import operator


operation_map = {
    '+': operator.add,
    '-': operator.sub
}

frequency_seen = []
frequency=0
frequency_found = False;

with open('day1_1_input.txt') as f:
    while frequency not in frequency_seen:
        frequency_seen.append(frequency)
        try:
            line = next(f)
        except StopIteration:
            f.seek(0)
            line = next(f)
        line = line.rstrip("\n")
        operator = operation_map[line[0]]
        frequency = operator(frequency, int(line[1:]))

print(frequency)
