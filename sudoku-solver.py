# first we take input from every row
# insert the value with spaces
row1 = list(map(int, input("Enter values of row1: ").split()))
row2 = list(map(int, input("Enter values of row2: ").split()))
row3 = list(map(int, input("Enter values of row3: ").split()))
row4 = list(map(int, input("Enter values of row4: ").split()))
row5 = list(map(int, input("Enter values of row5: ").split()))
row6 = list(map(int, input("Enter values of row6: ").split()))
row7 = list(map(int, input("Enter values of row7: ").split()))
row8 = list(map(int, input("Enter values of row8: ").split()))
row9 = list(map(int, input("Enter values of row9: ").split()))

# we will create a sudoku board using all the inputs
board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]


def solve(_board):
    """[take sudoku board as input and recursively check for the solution]
    
    Arguments:
        _board {[list]} -- [sudoku board]
    
    Returns:
        [bool] -- [True if it's empty and then solve it and False if already solved]
    """
    # first we check if a place is empty or not
    # if it's empty them it will return the position of that place
    empty = is_empty(_board)

    # if it's not empty that means it's already solved
    if not empty:
        return True
    else: # if it's empty then we extract the position from tuple
        row, col = empty
    
    # we will check a valid value for the number using our validator function
    for i in range(1, 10):
        if validator(_board, i, (row, col)):
            _board[row][col] = i

            if solve(_board):
                return True
            
            _board[row][col] = 0

    return False


def validator(_board, num, pos):
    """[it will take three arguments sudoku board, number to check for validaty and
        position on that we want to check the validaty of the number and will return 
        the bool value according the condition]
    
    Arguments:
        _board {[list]} -- [sudoku board]
        num {[int]} -- [number to check for validaty]
        pos {[tuple]} -- [position on that we want to check validaty]
    
    Returns:
        [bool] -- [True or False]
    """

    # checking rows
    for i in range(len(_board[0])):
        if _board[pos[0]][i] == num and pos[1] != i:
            return False

    # checking columns
    for i in range(len(_board)):
        if _board[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if _board[i][j] == num and (i, j) != pos:
                return False
    
    return True


def print_board(_board):
    """[it will sudoku board as input and print it in boxed represantation]
    
    Arguments:
        _board {[list]} -- [sudoku board]
    """
    for i in range(len(_board)):
        if i % 3 == 0 and i != 0:
            print('------------------------')
        for j in range(len(_board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")
            
            if j == 8:
                print(_board[i][j]) 
            else :
                print(str(_board[i][j]) + " ", end="")


def is_empty(_board):
    """[it will sudoku board as input and return the positon
        of empty positions as a tuple in row and col]
    
    Arguments:
        _board {[list]} -- [take the sudoku board as input]
    
    Returns:
        [tuple] -- [position as a tuple of row and colomn if position is empty]
    """
    for i in range(len(_board)):
        for j in range(len(_board[0])):
            if _board[i][j] == 0:
                return (i, j) # return tuple of i => row and j => colomn
    
    return None

# solvig the board by calling function on sudoku board
solve(board)
print("<--------------------->")
print_board(board)
