#!/usr/bin/env python3
# author: Ajil Raju <ajilraju01@gmail.com>

import random as rand

class Tictactoe():

    # Global board variable for the game pad
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # makers tuple for player1 and player2 marker
    markers = ('#', 'X', 'O')

    def __init__(self):
        pass
    def draw_board(self, board):
        print('\t.............')
        print('\t| {} | {} | {} |'.format(board[6], board[7], board[8]))
        print('\t----+---+----')
        print('\t| {} | {} | {} |'.format(board[3], board[4], board[5]))
        print('\t----+---+----')
        print('\t| {} | {} | {} |'.format(board[0], board[1], board[2]))
        print('\t.............')


    def win_check(self, board, player):
        """ check the equality of distinct 3 rows and same columns may contains same
            marker, at different dimensions """

        return ((board[0] == board[1] == board[2] == markers[player]) or    # check across bottom row
                (board[3] == board[4] == board[5] == markers[player]) or    # check across middle row
                (board[6] == board[7] == board[8] == markers[player]) or    # check across top row
                (board[0] == board[4] == board[8] == markers[player]) or    # check across diagonal 1,5,9
                (board[2] == board[4] == board[6] == markers[player]) or    # check across diagonal 2,5,7
                (board[0] == board[3] == board[6] == markers[player]) or    # check across first column
                (board[1] == board[4] == board[7] == markers[player]) or    # check across second column
                (board[2] == board[5] == board[8] == markers[player]))      # check across third column


    def check_draw(self):
        """ Check every rows and columns are filled with markers """
        return ' ' not in board[::-1]


    def check_space(self, pos):
        """ Check if any space is left for the next for the players """
        if board[int(pos) - 1] == ' ':
            return True
        else:
            return False


    def choose_position(self, player):
        """ Prompting the players to choose the desired position for the
            game moves and return back the position to control """
        position = 0
        while position not in range(1, 10) or not check_space(position):
            prompt = 'Player {} :Choose your next position (1-9) -> '.format(player)
            position = int(input(prompt))
        return position


    def place_marker(self, player, position):
        """ fill up the marker at the given position, here position is taken as
            (pos - 1) that is becuse, list index started with zero, human decide
            pos is started with 1 """
        board[position - 1] = markers[player]   # allocating markers at the indexed - 1 location.


    def replay(self):
        return input('\nDo you want to play again? Enter Yes or No:  ').lower().startswith('y')

    def welcome_notes():
        print("""
        Welcome to Tic Tac Toe!
         _ _ _
        |_|_|_|     7 8 9
        |_|_|_| --> 4 5 6
        |_|_|_|     1 2 3
             """)

class RandomPlayer():
    def __init__(self):
        pass

    def who_play_first():
        """ A random routines to select the player from choice of (1 and 2) """
        return rand.choice((1, 2))





    # main
while True:
    welcome_notes()
    toggle_player = RandomPlayer.who_play_first()
    player = toggle_player
    print('Player {} will go first :) '.format(player))
    is_start = input("Are you ready to play? Enter Yes or No. ")
    if is_start == 'Yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        play = Tictactoe()
        play.draw_board(play.board)
        position = play.choose_position(player)
        play.place_marker(player, position)
        if play.win_check(play.board, player):
            play.draw_board(play.board)
            print('\nCongratulations!!! Player {} Won the game !!!\n'.format(player))
            game_on = False
        else:
            if check_draw():
                play.draw_board(board)
                print('\nThe game is a draw! \n')
                break
            else:                   # Toggling the player1 to player2 and vice-versa
                if player == 1:
                    player = 2
                else:
                    player = 1

    # Reset the board for the new game, if any.
    board = [' '] * 9
    if not play.replay():
        break
