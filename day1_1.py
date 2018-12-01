import urllib.request
import operator


operation_map = {
    '+': operator.add,
    '-': operator.sub
}


frequency=0
with open('day1_1_input.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        operator = operation_map[line[0]]
        frequency = operator(frequency, int(line[1:]))

print(frequency)
