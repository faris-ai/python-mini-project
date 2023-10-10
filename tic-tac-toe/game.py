import time
from player import RandomComPlayer, HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range (9)]
        self.winner = None

    def print_board(self):
        chosen_board = [self.board[i*3:(i+1)*3] for i in range(3)]
        ind_row = 0
        for row in chosen_board:
            printed = '  ' + ' | '.join(row) + '  '
            print(printed)
            printed_dash = ""
            for dash in range(len(printed)):
                printed_dash+="-"
            print(printed_dash) if ind_row != len(chosen_board)-1 else None
            ind_row += 1

    @staticmethod
    def print_board_nums():
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        # print(number_board)
        for row in number_board:
            printed = '  ' + ' | '.join(row) + '  '
            print(printed)
            printed_dash = ""
            for dash in range(len(printed)):
                printed_dash+="-"
            print(printed_dash) if row != number_board[len(number_board)-1] else None

    def available_move(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, letter, square):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.decide_winner(letter,square):
                self.winner = letter
            return True
        return False
    
    def decide_winner(self, letter, chosen_square):
        # check row
        row_ind = chosen_square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = chosen_square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonal
        if chosen_square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal1]):
                return True
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

    def play(game, x_player, o_player, print_game = True):
        if print_game:
            game.print_board_nums()

        letter = 'X'

        while game.empty_squares():
            if letter == 'O':
                chosen_square = o_player.move(game)
            else:
                chosen_square = x_player.move(game)

            if game.make_move(letter, chosen_square):
                if print_game:
                    print(letter+f" makes move at square {chosen_square+1}")
                    game.print_board()
                    print()

                if game.winner:
                    if print_game:
                        print(f"{letter} wins!")
                    return letter

                letter = 'O' if letter == 'X' else 'X'
            
            time.sleep(1)

        if print_game:
            print("It\'s a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    game = TicTacToe()
    game.play(x_player,o_player)
    
# TicTacToe.print_board_nums()

