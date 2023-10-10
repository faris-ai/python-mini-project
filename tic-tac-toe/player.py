import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def move(self, letter):
        pass

class RandomComPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, game):
        chosen_square = random.choice(game.available_move())
        return chosen_square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            chosen_square = input(self.letter + "\'s move turn. Input move (1-9): ")
            try:
                val = int(chosen_square)-1
                if val not in game.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try Again!")
            print()
        return val

