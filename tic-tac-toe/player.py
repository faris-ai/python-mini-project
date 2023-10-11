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
    
class SmartComPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, game):
        if len(game.available_move()) == 9:
            chosen_square = random.choice(game.available_move())
        else:
            chosen_square = self.minimax(game, self.letter)['position']
        return chosen_square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_move():
            state.make_move(player, possible_move)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
