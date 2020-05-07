#!/usr/bin/env python3
#author: Ajil Raju <ajilraju01@gmail.com>

import random as rand

# Global board variable for the game pad
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# makers tuple for player1 and player2 marker
markers = ('#', 'X', 'O')

def draw_board(board):
    print('\t.............')
    print('\t| {} | {} | {} |'.format(board[6], board[7], board[8]))
    print('\t----+---+----')
    print('\t| {} | {} | {} |'.format(board[3], board[4], board[5]))
    print('\t----+---+----')
    print('\t| {} | {} | {} |'.format(board[0], board[1], board[2]))
    print('\t.............')

def win_check(board, player):
    return ((board[0] == board[1] == board[2] == markers[player]) or    # check across bottom row
    (board[3] == board[4] == board[5] == markers[player]) or            # check across middle row
    (board[6] == board[7] == board[8] == markers[player]) or            # check across top row
    (board[0] == board[4] == board[8] == markers[player]) or            # check across diagonal 1,5,9
    (board[2] == board[4] == board[6] == markers[player]) or            # check across diagonal 2,5,7
    (board[0] == board[3] == board[6] == markers[player]) or            # check across first column
    (board[1] == board[4] == board[7] == markers[player]) or            # check across second column
    (board[2] == board[5] == board[8] == markers[player]))              # check across third column

def check_draw():
    return (' ' not in  board[::-1])

# Check for the further allocation of markers
def check_space(pos):
    if board[int(pos) - 1] == ' ':
        return True
    else:
        return False

def choose_position(player):
    position = 0
    while position not in range(1, 10) or not check_space(position):
        prompt = 'Player {} :Choose your next position (1-9) -> '.format(player)
        position = int(input(prompt))
    return position

def place_marker(player, position):
    board[position - 1] = markers[player]   # allocating markers at the indexed - 1 location.

def replay():
    return input('\nDo you want to play again? Enter Yes or No:  ').lower().startswith('y')

def who_play_first():
    return rand.choice((1, 2))

# main
while True:
    print("""
    Welcome to Tic Tac Toe!
     _ _ _
    |_|_|_|     7 8 9    
    |_|_|_| --> 4 5 6
    |_|_|_|     1 2 3
    """)
    
    toggle_player = who_play_first();
    player = toggle_player
    print('Player {} will go first :) '.format(player))
    is_start = input("Are you ready to play? Enter Yes or No. ")
    if is_start == 'Yes':
        game_on = True
    else: 
        game_on = False

    while game_on:
        draw_board(board)
        position = choose_position(player)        
        place_marker(player,position)
        if win_check(board, player):
            draw_board(board)
            print('\nCongratulations!!! Player {} Won the game !!!\n'.format(player))
            game_on = False    
        else:
            if check_draw():
                draw_board(board)    
                print('\nThe game is a draw! \n')
                break
            else:                   # Toggling the player1 to player2 and vice-versa
                if player == 1:
                    player = 2
                else:
                    player = 1

    # Reset the board for the new game, if any.
    board = [' '] * 9    
    if not replay():            
        break
