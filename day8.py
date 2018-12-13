import sys

sys.setrecursionlimit(5000)

puzzle_input = []


class Node:
    def __init__(self, number_of_children, number_of_metadata, parent=None):
        self.number_of_children = number_of_children
        self.number_of_metadata = number_of_metadata
        self.metadata = []
        self.parent = parent
        self.children = []

    @property
    def has_all_children(self):
        return len(self.children) == self.number_of_children

    @property
    def sum_meta_data(self):
        meta_data_sum = sum(self.metadata)
        for child in self.children:
            meta_data_sum = meta_data_sum + child.sum_meta_data
        return meta_data_sum

    @property
    def value(self):
        if not self.children:
            return sum(self.metadata)

        node_value = 0
        for child_index in self.metadata:
            index = child_index-1
            try:
                child = self.children[index]
                node_value = node_value + child.value
                print(node_value)
            except IndexError:
                pass
        return node_value

    def __repr__(self):
        return f'{self.number_of_children} {self.number_of_metadata} {self.metadata}'


with open('day8.txt') as f:
    line = next(f)
    line = line.rstrip('\n')
    puzzle_input = [int(num) for num in line.split(' ')]


root_node = Node(puzzle_input[0], puzzle_input[1])

new_input = puzzle_input[2:]

current_parent_node = root_node
while(current_parent_node):
    if not current_parent_node.has_all_children:
        new_node = Node(new_input[0], new_input[1], current_parent_node)
        new_input = new_input[2:]
        current_parent_node.children.append(new_node)
        current_parent_node = new_node
    else:
        metadata = new_input[:current_parent_node.number_of_metadata]
        current_parent_node.metadata = metadata
        current_parent_node = current_parent_node.parent
        new_input = new_input[len(metadata):]


first_puzzle_result = root_node.sum_meta_data

print(f'The first puzzle result is {first_puzzle_result}')

second_puzzle_result = root_node.value

print(f'The second puzzle result is {second_puzzle_result}')
