from collections import Counter
number_of_players = 411

last_marble_value = 7105800


class Marble:
    def __init__(self, data, previous_marble=None, next_marble=None):
        self.data = data
        self.previous_marble = previous_marble
        self.next_marble = next_marble


class Game:
    def __init__(self, number_of_players, last_marble_value):
        self.number_of_players = number_of_players
        self.last_marble_value = last_marble_value
        self.score = {}
        self.turn = 0
        self.current_marble = Marble(0)
        self.current_marble.previous_marble = self.current_marble
        self.current_marble.next_marble = self.current_marble

    def play(self):
        self.turn = self.turn + 1
        if (self.turn % 23):
            new_marble = Marble(self.turn)

            # Set new marble's pointers
            new_marble.previous_marble = self.current_marble.next_marble
            new_marble.next_marble = \
                self.current_marble.next_marble.next_marble

            # insert new marble
            new_marble.previous_marble.next_marble = new_marble
            new_marble.next_marble.previous_marble = new_marble

            self.current_marble = new_marble
        else:
            marble_to_remove = self.current_marble.previous_marble
            for x in range(0, 6):
                marble_to_remove = marble_to_remove.previous_marble

            self.score[self.current_player] = self.score.get(
                self.current_player, 0) + marble_to_remove.data + self.turn
            self.current_marble = marble_to_remove.next_marble
            marble_to_remove.previous_marble.next_marble = \
                marble_to_remove.next_marble
            marble_to_remove.next_marble.previous_marble = \
                marble_to_remove.previous_marble

    @property
    def current_player(self):
        return ((self.turn - 1) % self.number_of_players) + 1

    @property
    def is_finished(self):
        return self.turn >= self.last_marble_value

    def show_state(self):
        marble = self.current_marble
        state = f'[{self.current_player}] ({marble.data})'
        while marble.next_marble is not self.current_marble:
            marble = marble.next_marble
            state = f'{state} {marble.data}'
        print(state)


game = Game(number_of_players, last_marble_value)

while not game.is_finished:
    game.play()
    # game.show_state()

print(
    f'The answer of the puzzle is {Counter(game.score).most_common(1)[0][1]}')
