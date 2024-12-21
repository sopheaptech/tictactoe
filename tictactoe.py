# tictactoe
# Main
import os
# # Welcome Function
# def welcome():
#     print("Welcome to Tec Toc Toe Game!")
#     print("Please Enjoy Playing :)")

# Display board function
def display_board(board):
    os.system('cls')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# Player input
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player : Choose X or O: ")
        marker = marker.upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# Place Marker on board
def place_marker(board, marker, position):

    board[position] = marker

# Check Winner
# We have 4 Conditions to check

def check_winner(board, marker):
    # Check Rows Condition
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or # Check First Row Condition
            (board[4] == board[5] == board[6] == marker) or # Check Second row condition
            (board[7] == board[8] == board[9] == marker) or # Check third row condition
            (board[1] == board[4] == board[7] == marker) or # Check First Column condition
            (board[2] == board[5] == board[8] == marker) or # Check Second Column condition
            (board[3] == board[6] == board[9] == marker) or # Check third Column Condition
            (board[1] == board[5] == board[9] == marker) or # Check left-bottom diagonals
            (board[3] == board[5] == board[7] == marker))   # Check right-bottom diagonals


# Create Choose First for player Function import random modula using random.randint()
import random
def choose_first():
    choice = random.randint(0, 1)
    if choice == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Check Free Space Function to if it's available space or not to return True or False
def cheeck_freeSpaces(board, position):
    return board[position] == ' '

# Create function that check the board is full or not
def fullboard_check(board):
    for i in range(1,10):
        if cheeck_freeSpaces(board, i):
            return False
    # BOARD IS FULL RETURN TRUE
    return True 


# Create Player choice Function
# *Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses 
# the function from step 6 to check if its a free position. If it is, then return the position for later use. *

def player_choice(board):
    position = 0
    while position not in range(1,10) or not cheeck_freeSpaces(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position
    

# Replay Function
def replay():
    choice = input("Would You Like to play again? Yes/No: ").upper()
    return choice == 'YES'


# Function  Logical Order Last Step Call Function in Logic
# There are some step to do 


# CREATE WHILE LOOP TO KEEP GAME RUNNING
print("\n")
print("Welcome To Tic-Tac-Toe :)")
print("---------------------------")
print("\n")
while True:
    # PLAY THE GAME
    ## Set Everything up (display board, Who go First, Player choose X or O)
    the_board = [' '] *10 # or With 2D list board = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Will go first')
    play_game = input("Ready to play? Y or N: ").upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    ### GAME PLAY
    while game_on:

        #### PLAYER 1 TURN

        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place marker on position
            place_marker(the_board, player1_marker, position)
            # Check Winner
            if check_winner(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON !")
                game_on = False # You can say break is ok because we want break while loo
            # Check if it's a Tie, No one won the game
            else:
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("IT'S A TIE !")
                    game_on = False
                else:
                    turn = 'Player 2'

        ##### PLAYER 2 TURN

        else:
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place marker on position
            place_marker(the_board, player2_marker, position)
            # Check Winner
            if check_winner(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON !")
                game_on = False # You can say the break is ok because we want a break while loo
            # Check if it's a Tie, No one won the game
            else:
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("IT'S A TIE !")
                    game_on = False
                else:
                    turn = 'Player 1'

    # BREAK OUT OF On replay()
    if not replay():
        break




