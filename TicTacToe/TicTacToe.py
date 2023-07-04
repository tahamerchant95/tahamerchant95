# need to print tictac board
# user will first decide to become 'X' or 'Y'
# need to filter of combinations as to how user can win
# there will be two players playing the game 
# user can win with straight Xs either horizontal or vertical
# user can win with diagonal Xs
# 8 possible winning combinations 
# program will decide if game is won, tied, lost
# code will need to check if player 1 has already taken the position on board
# the board can be visualized through the keyboard keypad
# every user will have five moves on which will be decided if the game has won or lost or tied
# players need to be changed after every move 
# for instance if player 1 is X and makes move then its player2s turn 
# board needs to be updated after every move 
# program needs to decide who goes first
# first we will define all functions and then create full game logic 


import random 

import time 

def display_board(board): # will first try to draw our board
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
def user_character(): # function that assigns x or o to players
    player2= ''
    player1= input("Which character do you want to be? (x or o)")
    player1=player1.lower() # since we are using lowcase letters

    if player1 == "x":
        print("\nplayer 1 you are 'x'")
        player2 == "o"
    else:
        player2 == "x"
        print("\nplayer 2 you are 'o'")
        return(player1,player2)
    
def is_Winner(board, character): #will create winning combos
    return  ((board[7]==character and board[8]==character and board[9]==0) 
        or  (board[4]==character and board[5]==character and board[6]==character) or 
            (board[1]==character and board[2]==character and board[3]== character) or 
            (board[7]==character and board[5]== character and board[3]==character)or
            (board[9]==character and board[5]==character and board[1]==character) or
            (board[7]==character and board[4]==character and board[1]==character) or 
            (board[8]==character and board[5]==character and board[2]==character)or
            (board[9]==character and board[6]==character and board[3]==character))
    

def moves(board,character,position): # player makes on the move, where letter is entered on board and equates to our position
    board[character]= position

def free_space(board,position): # will check if there are free spaces on board 
    return board[position]== ' '


def full_board(board): #will have to check if board is full 
    for chars in range(1,10):
        if free_space(board, chars):
            print("\nstill have space on board")
        else:
            print("\nBoard is full")

def players_moves(board): # the position that user needs to enter on the board
    position= ' '

    while position not in '1,2,3,4,5,6,7,8,9'.split() or not free_space(board, int(position)): # casted position to integer value
        print("\nyour next move from (1-9)")
        position=input()
    return int(position)

def first_player():
    choice= random.randint(0,1)

    if choice == 0:
        return 'Player1'
    else:
        return 'Player2'
    

while True:
    rst_board=[' '] * 10 
    player_character= user_character()
    turn= first_player()
    print("First player will be " + turn + " who will go first")
    game_play= True 

    while game_play:
        if turn == 'Player1':
            display_board(rst_board)
            move= players_moves(rst_board)
            moves(rst_board,player_character, move)

            if is_Winner(rst_board,player_character):
                display_board(rst_board)
                move= players_moves(rst_board)
                print("\n You have won the game!")
                game_play=False
            else:
                if full_board(rst_board):
                    display_board(rst_board)
                    print("\n Game is tied")
                    break
                else:
                    turn='Player2'
