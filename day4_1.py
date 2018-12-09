import re
from datetime import datetime
from collections import Counter

puzzle_input = []
with open('day4_1_input.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        date_match = re.search('^\[(.+)\]\s(.+)$', line)

        date_string, instruction = date_match.groups()

        line_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
        puzzle_input.append((line_date, instruction))

puzzle_input.sort(key=lambda tup: tup[0])

guard_dict = {}

for puzzle_date, instruction in puzzle_input:
    if instruction.endswith('begins shift'):
        guard_id = int(re.search('(\d+)', instruction).groups()[0])
        if guard_id not in guard_dict:
            guard_dict[guard_id] = []
        last_instruction_date = puzzle_date

    elif instruction.endswith('falls asleep'):
        last_instruction_date = puzzle_date

    elif instruction.endswith('wakes up'):
        asleep_range = range(last_instruction_date.minute, puzzle_date.minute)
        guard_dict[guard_id].extend([ minute for minute in asleep_range])

max_minute_asleep = 0
guard_most_asleep = 0

minute_most_asleep = 0
guard_with_minute_most_asleep = 0
max_number_of_time_asleep = 0


for guard_id, guard_minutes_asleep in guard_dict.items():
    number_of_minutes_asleep = len(guard_minutes_asleep)
    if number_of_minutes_asleep > max_minute_asleep:
        max_minute_asleep = number_of_minutes_asleep
        guard_most_asleep = guard_id

    if guard_minutes_asleep:
        minute, number_of_time_asleep = Counter(guard_minutes_asleep).most_common(1)[0]
        if number_of_time_asleep > max_number_of_time_asleep:
            guard_with_minute_most_asleep = guard_id
            minute_most_asleep = minute
            max_number_of_time_asleep = number_of_time_asleep

max_minutes = Counter(guard_dict[guard_most_asleep]).most_common(1)[0][0]

print(f'the most asleep guard in {guard_most_asleep} and the minute is {max_minutes}')
print(f'The answer of the puzzle is {2411*42}')


print(f'The answer of puzzle two is {guard_with_minute_most_asleep} * {minute_most_asleep} = {guard_with_minute_most_asleep * minute_most_asleep}')
