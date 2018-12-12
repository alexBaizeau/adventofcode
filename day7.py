import re
from string import ascii_uppercase

class Step:
    def __init__(self, letter):
        self.letter = letter
        self.prerequisites = set()
        self.reset_work()

    def is_available(self, completed_steps):
        return not self.is_started and not self.is_completed and self.prerequisites.issubset(set(completed_steps))

    def complete(self):
        self.is_started = False
        self.is_completed = True

    def tick(self):
        self.is_started = True
        self.amount_of_work = self.amount_of_work - 1
        if self.amount_of_work < 1:
            self.amount_of_work = 0
            self.complete()

    def reset_work(self):
        self.is_completed = False
        self.is_started = False
        self.amount_of_work = 61 + ascii_uppercase.index(self.letter)

    def __hash__(self):
        return ord(self.letter)

    def __eq__(self, other):
        return other.letter == self.letter


puzzle_answer = ''
all_steps_by_letters = {}

regexp = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin\.'
with open('day7.txt') as f:
    for line in f:
        prerequisite_letter, step_letter = re.search(regexp, line).groups()
        step = all_steps_by_letters.get(step_letter)
        prerequisite_step = all_steps_by_letters.get(prerequisite_letter)

        if not prerequisite_step:
            prerequisite_step = Step(prerequisite_letter)
            all_steps_by_letters[prerequisite_letter] = prerequisite_step
        if not step:
            step = Step(step_letter)
            all_steps_by_letters[step_letter] = step
        step.prerequisites.update({prerequisite_step})


done = False
while not done:
    completed_steps = [step for _, step in all_steps_by_letters.items() if step.is_completed]
    available_steps = [step for _, step in all_steps_by_letters.items() if step.is_available(completed_steps)]

    if available_steps:
        available_steps.sort(key=lambda step: step.letter)
        available_steps[0].complete()
        puzzle_answer = puzzle_answer + available_steps[0].letter
    else:
        done = True


print(f'The answer to the first puzzle is {puzzle_answer}')


# For the second part of the puzzle we reset everything

for _, step in all_steps_by_letters.items():
    step.reset_work()

ticks = 0
number_of_workers = 5
done = False
while not done:

    started_steps = [step for _, step in all_steps_by_letters.items() if step.is_started]
    completed_steps = [step for _, step in all_steps_by_letters.items() if step.is_completed]
    available_steps = [step for _, step in all_steps_by_letters.items() if step.is_available(completed_steps)]

    steps_worked_on = started_steps[:number_of_workers]
    inactive_workers = number_of_workers - len(steps_worked_on)
    steps_worked_on += available_steps[:inactive_workers]

    if steps_worked_on:
        for step in steps_worked_on:
            step.tick()
        ticks = ticks + 1
    else:
        done = True

print(f'The answer to the second puzzle is {ticks}')
