from random import randrange
import numpy as np

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f'''
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+''')
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision
    free_fields = make_list_of_free_fields(board)
    valid_move = False

    while(valid_move == False):
        try:
            selection = int(input("Enter your move: "))
            if (selection > 9 or selection < 1):
                print("Select a number between 1 and 9")
                continue
            else:
                (row,col) = ((selection - 1) // 3, (selection - 1) % 3)
            
                if ((row,col) in free_fields):
                    board[row][col] = 'o'
                    valid_move = True
                else:
                    print("Invalid move, spot already taken")     
        except ValueError:
            print("The selection isn't a valid number")
 

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(len(board)):
        for col in range(len(board)):
            coord = (row, col)
            if board[row][col] != "x" and board[row][col] != "o":
                free_fields.append(coord)

    return free_fields

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    free_fields = make_list_of_free_fields(board)
    board_transpose = [[row[i] for row in board] for i in range(3)]
    main_diagonal = [board[i][i] for i in range(3)]
    counter_diagonal = [board[i][2-i] for i in range(3)]
    board_diagonals = [main_diagonal,counter_diagonal,[0,0,0]]

    # Check for rows, columns and both diagonals
    for rows,columns,diagonals in zip(board,board_transpose,board_diagonals):
        if (rows.count('x') == 3 or columns.count('x') == 3 or diagonals.count('x') == 3):
                return False,'x' 
        elif (rows.count('o') == 3 or columns.count('o') == 3 or diagonals.count('o') == 3):
                return False,'o'
    if(len(free_fields) < 1):
        return False,'tie'

    return True,'null'

def two_consecutive_check(board):
    # The function analyzes the board's status in order to check if 
    # the player has two consecutive marks in the board and the selection becomes 
    # the remaining square in order to stop the user from winning
    board_transpose = [[row[i] for row in board] for i in range(3)]
    main_diagonal = [board[i][i] for i in range(3)]
    counter_diagonal = [board[i][2-i] for i in range(3)]
    board_diagonals = [main_diagonal,counter_diagonal,[0,0,0]]

    # Check for rows, columns and both diagonals
    for rows,columns,diagonals in zip(board,board_transpose,board_diagonals):
        if (rows.count('o') == 2 and rows.count('x') == 0):
                return rows
        elif(columns.count('o') == 2 and columns.count('x') == 0):
                return columns
        elif(diagonals.count('o') == 2 and diagonals.count('x') == 0):
                return diagonals

    return []

def draw_move_E(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    active_game,winner = victory_for(board)
    if (active_game == False):
        return
    
    valid_move = False
    while(valid_move == False):
        selection = randrange(9)
        (row,col) = ((selection - 1) // 3, (selection - 1) % 3)
        if(len(free_fields) > 0):
            if ((row,col) in free_fields):
                board[row][col] = 'x'
                valid_move = True

def draw_move_H(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    user_consecutive_marks = two_consecutive_check(board)
    active_game,winner = victory_for(board)
    if (active_game == False):
        return
    
    print(user_consecutive_marks)

    if (len(user_consecutive_marks) > 1):
         for item in user_consecutive_marks:
              
              if (item != 'o'):
                   row,col = ((item - 1) // 3, (item - 1) % 3)
                   board[row][col] = 'x'
                   return
         
    valid_move = False
    while(valid_move == False):
        selection = randrange(9)
        (row,col) = ((selection - 1) // 3, (selection - 1) % 3)
        if(len(free_fields) > 0):
            if ((row,col) in free_fields):
                board[row][col] = 'x'
                valid_move = True

def start_game(dif):
    active_game = True
    if (dif == "h"):
        while(active_game):
            enter_move(board)
            active_game,winner = victory_for(board)
            draw_move_H(board)
            active_game,winner = victory_for(board)
            display_board(board)
        if(winner == 'o'):
            print("Congratulations, you won!")
        elif(winner == 'tie'):
            print("It's a tie!")
        else:
            print("The machine wins!")
    else:
        while(active_game):
            enter_move(board)
            active_game,winner = victory_for(board)
            draw_move_E(board)
            active_game,winner = victory_for(board)
            display_board(board)
        if(winner == 'o'):
            print("Congratulations, you won!")
        elif(winner == 'tie'):
            print("It's a tie!")
        else:
            print("The machine wins!")

# Main Code #
if __name__ == "__main__":
    board = [[1,2,3],[4,5,6],[7,8,9]]

    difficulty = input("Welcome to TicTacToe, choose your difficulty (E)asy || (H)ard: ")
    difficulty.lower()
    display_board(board)
    start_game(difficulty)

# Test Functions #
# test_board = [['o','o',3],[4,5,6],[7,8,9]]
# draw_move_H(test_board)


