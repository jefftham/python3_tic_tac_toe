# -*- coding: utf-8 -*-

"""
    A simple Tic Tac Toe Game that written in python.
    This game can be played in commant-line.
    
    Requirements:
        * 2 players should be able to play the game (both sitting at the same computer)
        * The board should be printed out every time a player makes a move
        * You should be able to accept input of the player position and then place a symbol on the board
        * game will be restarted if you click 0.
"""

# switch between two player
from itertools import cycle
myIterator = cycle(range(2))

# create a list that intended to save numpad key from 1 to 9, the 0 index is not used.
board = [ ' ' for x in range(10)]
board[0] = 0
         
# define players marker
players ={1:'O', 2:'X'}

#if there is a winner:
gotWinner = False
         
# define the board
def print_board(board):
    
    #extra line
    print()
    
    #upper line
    print('{b7}|{b8}|{b9}'.format(b7=board[7],b8=board[8],b9=board[9]))
    print('-----')
    
    #middle line
    print('{b4}|{b5}|{b6}'.format(b4=board[4],b5=board[5],b6=board[6]))
    print('-----')
    
    #lower line
    print('{b1}|{b2}|{b3}'.format(b1=board[1],b2=board[2],b3=board[3]))


# input value to the board
def input_board(player, position, board):
    
    # marker for player 1 is O; player 2 is X
    
    if player not in players:
        print("invalid player code")
    else:
        board[position] = players[player]

    print_board(board)
    
    return check_winner(player,board )

        

# check if someone win
def check_winner(player, board):
   
   #check if no more move
   if board.count(' ') == 0:
       print("Tie game: no more move")
       return True
    
   if player not in players:
        print("invalid player code")
   else:
        if ((board[7] == board[8] == board[9] and board[9]!= ' ') or
            (board[4] == board[5] == board[6] and board[6]!= ' ') or
            (board[1] == board[2] == board[3] and board[3]!= ' ') or
            (board[7] == board[4] == board[1] and board[1]!= ' ') or
            (board[8] == board[5] == board[2] and board[2]!= ' ') or
            (board[9] == board[6] == board[3] and board[3]!= ' ') or
            (board[7] == board[5] == board[3] and board[3]!= ' ') or
            (board[9] == board[5] == board[1] and board[1]!= ' ' ) ): 
                print("player "+str(player)+" won")
                return True
        else:
            return False
    
# start the game and show the rules
def start():
    print()
    print("It is a normal 2 people Tic Tac Toe Game without 'non-player character (NPC)'")
    print("player 1 is 'O' , player 2 is 'X'")
    print("please click the numpad for you input")
    
    reset()
    global gotWinner
    global board
    print_board(board)
    print("player 1 can move now")
    
    next_player = next(myIterator) +1
    next_one = lambda: input_board(next_player, read_input(), board)
    gotWinner = next_one()
    while gotWinner != True:
        
        next_player = next(myIterator) +1
        print("player "+str(next_player) +" turn")        
        gotWinner = next_one()
    else:
        print("do you want to play again?")
        print("'y' for yes, 'n' for no")
        play_again = str(input())
        if play_again == 'y':
            start()
        else:
            print("bye bye")
            #exit(0)
            
# reset the game
def reset():
    global board
    board = [ ' ' for x in range(10)]
    board[0] = 0
    
    global gotWinner
    gotWinner = False
    
    global myIterator
    myIterator = cycle(range(2))

    
def read_input():
    global board
    try:
        new_move = int(input())
        if new_move == 0:
            start()
        elif board[new_move] != ' ':
            print('invalid option, the slot is not available.')
            print('please choose again')
            return read_input()
        else:
            return new_move             
    except ValueError:
        print("the input is not valid!!!")
        return read_input()
        
start()