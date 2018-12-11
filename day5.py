from string import ascii_lowercase

def react_line(line):
    had_reaction = True
    while(had_reaction):
        previous_character = line[0]
        for index, character in enumerate(line):
            had_reaction = False
            if character.upper() == previous_character.upper() and character != previous_character:
                line_list = list(line)
                del line_list[index]
                del line_list[index - 1]
                line = ''.join(line_list)
                had_reaction = True
                break
            previous_character = character
    return line

with open('day5_1.txt') as f:
    puzzle_line = f.readline().rstrip('\n')

line = react_line(puzzle_line)
print(f'the answer of the first puzzle is {len(line)}')


min_length = len(line)
character = 'a'

for character in ascii_lowercase:
    line = puzzle_line.replace(character, '')
    line = line.replace(character.upper(), '')
    line_length = len(react_line(line))
    if line_length < min_length:
        min_length = line_length
        min_character = character

print(f'the answer of the second puzzle is {min_length}')
