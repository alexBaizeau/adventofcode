import re

pattern = r"position=<\s?(-?\d+),\s*(-?\d+)>\svelocity=<\s?(-?\d+),\s*(-?\d+)>"


class Point():
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def rewind(self):
        self.x = self.x - self.velocity_x
        self.y = self.y - self.velocity_y


class Message():
    def __init__(self):
        self.points = []
        self.time = 0

    def tick(self):
        self.time = self.time + 1
        for point in self.points:
            point.move()

    def rewind(self):
        self.time = self.time - 1
        for point in self.points:
            point.rewind()

    @property
    def min_x(self):
        return min(self.points, key=lambda point: point.x).x

    @property
    def min_y(self):
        return min(self.points, key=lambda point: point.y).y

    @property
    def max_x(self):
        return max(self.points, key=lambda point: point.x).x

    @property
    def max_y(self):
        return max(self.points, key=lambda point: point.y).y

    @property
    def height(self):
        max_y = self.max_y
        min_y = self.min_y

        return max_y - min_y

    def __repr__(self):
        line = ''
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                character = '.'
                for point in self.points:
                    if point.x == x and point.y == y:
                        character = '#'
                line = line + character
            line = line + '\n'
        return line


message = Message()
with open('day10.txt') as f:
    for line in f:
        x, y, velocity_x, velocity_y = re.match(pattern, line).groups()
        point = Point(int(x), int(y), int(velocity_x), int(velocity_y))
        message.points.append(point)

previous_height = message.height

while(previous_height >= message.height):

    previous_height = message.height
    message.tick()


message.rewind()
print(message)
print(f'the elves had to wait {message.time}')
