def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    # check row
    row_val = puzzle[row]
    if guess in row_val:
        return False
    
    # check column
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False
    
    # check 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if guess == puzzle[r][c]:
                return False
            

    # if valid
    return True
    


def solve_sudoku(puzzle):
    
    # find empty puzzle to guess
    row, col = find_next_empty(puzzle)

    # if there's nowhere empty
    if row is None:
        return True
    
    # make guess between 1 and 9 at the empty puzzle
    for guess in range(1, 10):
        # check if the guess is valid
        if is_valid(puzzle, guess, row, col):
            # put the guess at the empty puzzle
            puzzle[row][col] = guess    
            # do the job recursively 
            if solve_sudoku(puzzle):
                return True
        
        # if the guess does not valid or does not solve the puzzle 
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_puzzle = [
        [-1, -1, -1, 4, -1, 3, 8, -1, -1],
        [5, -1, -1, -1, 9, -1, -1, -1, -1],
        [-1, 8, 6, -1, -1, -1, -1, -1, 7],
        [-1, -1, 5, 2, -1, -1, -1, 8, 4],
        [-1, 2, 1, -1, -1, -1, -1, 5, -1],
        [-1, -1, -1, -1, -1, -1, 7, -1, 9],
        [1, 5, -1, 7, -1, -1, 9, -1, 8],
        [4, 9, -1, -1, 1, -1, 2, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 7, 1]
    ]

    print(solve_sudoku(example_puzzle))
    print(example_puzzle)




