'''this is a program based around connect 4 the user can play simulation, single player and multiplayer game they
can also get graphs of the games and simulations finally they can do Testing hypotheses and changing parameters
to understand how these changes affect the games'''

#imports part of python's standard library
import time
import random as ra
import statistics
import csv
import os

#imports that may need to be installed
from prettytable import PrettyTable, HRuleStyle, VRuleStyle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# define lists for use later
turns = [] 
y_cols = []
y_rows = []
r_cols = []
r_rows = []
attack_y = []
attack_r = []
turn_list = []
turns_csv = []
defense_y = []
defense_r = []
neutral_y = []
neutral_r = []
row_y_list = []
row_r_list = []
game_types = []
atk_n_def_y = []
atk_n_def_r = []
first_column = []
column_y_list = []
column_r_list = []
win_draw_lose = []
win_lose_draw = []
all_mean_y_col = []
all_mean_y_row = []
all_mean_r_col = []
all_mean_r_row = []
games_outcomes  = [] 
game_outcome_list = []
pct_atk_def_n_list_y = []
pct_atk_def_n_list_r = []
mean_median_mode_list = []
atk_def_neutral_list_y = []
atk_def_neutral_list_r = []
percentage_atk_n_def_y = []
percentage_atk_n_def_r = []
percentage_win_draw_lose = []
percentage_atk_n_def_y_hyp = []
percentage_atk_n_def_r_hyp = []
percentage_atk_n_def_y_base = []
percentage_atk_n_def_r_base = []
percentage_win_draw_lose_hyp = []
percentage_win_draw_lose_base = []
percentage_win_draw_lose_base_hyp = []

#takes in user inputs and validates they are acceptable inputs if not it will ask for the input again
def user_clean_data(user, upper_limit, lower_limit):
    #this is for the game itself picking the row
    if upper_limit == 7:
        user_input = input(user + " Player input a number between " + str(lower_limit) + "-" + str(upper_limit) + ": ")
    #this is for the menus options picking the menu there is 4 or 5 option in all the menus this can cater to both
    elif upper_limit == 4 or upper_limit == 5:
        user_input = input("Input a number between " + str(lower_limit) + "-" + str(upper_limit) + ": ")
    #this is use to pick the number of simulations the user wants in simulation mode
    else:
        user_input = input("Input the number of simulations you require between " + str(lower_limit) + "-" + str(upper_limit) + ": ")
    #this check that the number is not a integer and is between not between lower_limit and upper_limit if that is True it goes into the loop and keep going until the user inputs a valid input
    while not (user_input.isnumeric() and lower_limit <= int(user_input) <= upper_limit):
        #prints: Input Invalid in red
        print("\x1b[1m\x1b[31mInput Invalid\x1b[0m\x1b[0m")
        #this is for the game itself picking the row
        if upper_limit == 7:
            user_input = input(user + " Player input a number between " + str(lower_limit) + "-" + str(upper_limit) + ": ")
        #this is for the menus options picking the menu there is 4 or 5 option in all the menus this can cater to both
        elif upper_limit == 4 or upper_limit == 5:
            user_input = input("Input a number between " + str(lower_limit) + "-" + str(upper_limit) + ": ")
        #this is use to pick the number of simulations the user wants in simulation mode
        else:
            user_input = input("Input the number of simulations you require between " + str(lower_limit) + "-" + str(upper_limit) + ": ")
    #turn the user_input into an integer and subtracts 1 as all background tasks start at 0 rather than 1
    user_input = int(user_input) - 1
    #returns user_input
    return user_input


# checks to see if the top row of the inputted column is full then return False if it is filled or True if it is not
def column_unfilled(board, column):
    return board[5][column] == 0


# finds the lowest row that is empty from the inputted column and returns that row
def gravity(board, column):
    for hole in range(6):
        if board[hole][column] == 0:
            return hole


# makes the board an 6x7 array fill with 0s
def make_board():
    clean_board = np.zeros((6, 7),)
    return clean_board
board = make_board()


#makes the front_end_board an 6x7 array fill with 0s this one can be filled with pointers to other python objects stored somewhere else
def front_end_board():
    zero_board = np.zeros((6, 7),dtype=object)
    return zero_board
front_board = front_end_board()


# flips the board as the numpy arrays consider the top left to be (0,0) but the it is easier to work with the the bottom left being (0,0)
def flip_board(board):
    flipped_board = (np.flip(board , 0))
    return flipped_board
board_right_way = flip_board(board) 


#checks if the board is a filled along the top row and if it is it returns True
def draw(board):
    for column in range(7):
        if board[0][column] == 0:
            return False
    return True


#checks for 2 in a row in the numpy array and and tries to make it 3 in a row
def three_in_a_row(board, chip):
    #defines board_right_way
    board_right_way = flip_board(board)
    #sets the default value back to be (-1 , -1)
    back = (-1 , -1)
    #iterates through a initial box of values in the array
#checks for 2 in a row vertically and looks for 3 in a row
    for x in range(7):
        for y in range(5):
            #checks for 2 in a row vertically from each x and y value given from above
            if board[y][x] == chip and board[y+1][x] == chip:
                #position of the connect 4 chip upwards
                next_move_large = y+3
                #position of the connect 4 chip downwards
                next_move_small = y-2
                #position of the connect 3 chip upwards
                large_y = 5-(y+2)
                #position of the connect 3 chip downwards
                small_y = 5-(y-1)
                
                #checking that the small_y and next_move_small will fit on the board
                if 5 >= small_y >= 0 and 5 >= next_move_small >= 0:
                    #small_three is equal to the value on (next_move_small,x)
                    small_three = board[next_move_small][x]
                    #small_col = the row gravity says x is on
                    small_col = gravity(board_right_way, x)
                    #if the rows match and the small_three has no chips back is give these value
                    if small_col == small_y and small_three == 0:
                        back = (y,x)
                
                #checking that the large_y and next_move_large will fit on the board
                if 5 >= large_y >= 0 and 5 >= next_move_large >= 0 :
                    #large_three is equal to the value on (next_move_large,x)
                    large_three = board[next_move_large][x]
                    #large_col = the row gravity says x is on
                    large_col = gravity(board_right_way, x)
                    #if the rows match and the large_three has no chips back is give these value
                    if large_col == large_y and large_three == 0:
                        back = (y,x)

#checks for 2 in a row horizontally and looks for 3 in a row                
    #if back has not already been set
    if back == (-1, -1):
        #iterates through a initial box of values in the array
        for y in range(6):
            for x in range(6):
                 #checks for 2 in a row horizontal from each x and y value given from above
                if board[y][x] == chip and board[y][x+1] == chip:
                    #position of the connect 4 chip to the right
                    next_move_large = x+3
                    #position of the connect 4 chip to the left
                    next_move_small = x-2
                    #position of the connect 3 chip to the right
                    large_x = x+2
                    #position of the connect 3 chip to the left
                    small_x = x-1
                    #to account for position of origin
                    y = 5-(y)
                    
                    #checking that the small_x and next_move_small will fit on the board
                    if 6 >= small_x >= 0 and 6 >= next_move_small >= 0:
                        #small_three is equal to the value on (y,next_move_small)
                        small_three = board_right_way[y][next_move_small]
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match and the small_three has no chips back is give these value
                        if small_col == y and small_three == 0:
                            back = (y, small_x)
                    
                    #checking that the small_x and large_x will fit on the board
                    if 6 >= small_x >= 0 and 6 >= large_x >= 0:
                        #small_three is equal to the value on (y,large_x)
                        small_three = board_right_way[y][large_x]
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match and the small_three has no chips back is give these value
                        if small_col == y and small_three == 0:
                            back = (y, small_x)
                    
                    #checking that the small_x and large_x will fit on the board
                    if 6 >= large_x >= 0 and 6 >= next_move_large >= 0:
                        #large_three is equal to the value on (y,next_move_large)
                        large_three = board_right_way[y][next_move_large]
                        #small_col = the row gravity says large_x is on
                        large_col = gravity(board_right_way, large_x)
                        #if the rows match and the large_three has no chips back is give these value
                        if large_col == y and large_three == 0:
                            back = (y, large_x)

#checks for 2 in a row in a positively diagonals and looks for 3 in a row
    #if back has not already been set
    if back == (-1, -1):
        #iterates through a initial box of values in the array
        for y in range(5):
            for x in range(6):
                #checks for 2 in a row in a positively diagonals from each x and y value given from above
                if board[y][x] == chip and board[y+1][x+1] == chip:
                    #position of the connect 4 chip to the right
                    next_move_large_x = x+3
                    #position of the connect 4 chip upwards
                    next_move_large_y = 5-(y+3)
                    #position of the connect 4 chip to the left
                    next_move_small_x = x-2
                    #position of the connect 4 chip downwards
                    next_move_small_y = 5-(y-2)
                    #position of the connect 3 chip to the right
                    large_x = x+2
                    #position of the connect 3 chip upwards
                    large_y = 5-(y+2)
                    #position of the connect 3 chip to the left
                    small_x = x-1
                    #position of the connect 3 chip downwards
                    small_y = 5-(y-1)
                    
                    #checking that the small_x, small_y,next_move_small_x and next_move_small_y will fit on the board
                    if 6 >= small_x >= 0 and 5 >= small_y >= 0 and 6 >= next_move_small_x >= 0 and 5 >= next_move_small_y >= 0:
                        #small_three is equal to the value on (next_move_small_y,next_move_small_x)
                        small_three = board_right_way[next_move_small_y][next_move_small_x]
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match and the small_three has no chips back is give these value
                        if small_col == small_y and small_three == 0:
                            back = (small_y, small_x)
                    
                     #checking that the large_x, large_y,next_move_large_x and next_move_large_y will fit on the board
                    if 6 >= large_x >= 0 and 5 >= large_y >= 0 and 6 >= next_move_large_x >= 0 and 5 >= next_move_large_y >= 0:
                        #large_three is equal to the value on (next_move_large_y,next_move_large_x)
                        large_three = board_right_way[next_move_large_y][next_move_large_x]
                        #large_col = the row gravity says large_x is on
                        large_col = gravity(board_right_way, large_x)
                        #if the rows match and the large_three has no chips back is give these value
                        if large_col == large_y and large_three == 0:
                            back = (large_y, large_x)

#checks for 2 in a row in a negative diagonals and looks for 3 in a row
    #if back has not already been set            
    if back == (-1, -1):
        #iterates through a initial box of values in the array
        for y in range(5):
            y+=1
            for x in range(6):
                #checks for 2 in a row in a negative diagonals from each x and y value given from above
                if board[y][x] == chip and board[y-1][x+1] == chip:
                    #position of the connect 4 chip to the right
                    next_move_large_x = x+3
                    #position of the connect 4 chip upwards
                    next_move_small_y = 5-(y+2)
                    #position of the connect 4 chip to the left
                    next_move_small_x = x-2
                    #position of the connect 4 chip downwards
                    next_move_large_y = 5-(y-3)
                    #position of the connect 3 chip to the right
                    small_y = 5-(y+1)
                    #position of the connect 3 chip upwards
                    large_x = x+2
                    #position of the connect 3 chip to the left
                    small_x = x-1
                    #position of the connect 3 chip downwards
                    large_y = 5-(y-2)
                    
                    #checking that the small_x, small_y,next_move_small_x and next_move_small_y will fit on the board
                    if 6 >= small_x >= 0 and 5 >= small_y >= 0 and 6 >= next_move_small_x >= 0 and 5 >= next_move_small_y >= 0:
                        #small_three is equal to the value on (next_move_small_y,next_move_small_x)
                        small_three = board_right_way[next_move_small_y][next_move_small_x]
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match and the small_three has no chips back is give these value
                        if small_col == small_y and small_three == 0:
                            back = (small_y, small_x)
                    
                    #checking that the large_x, large_y,next_move_large_x and next_move_large_y will fit on the board
                    if 6 >= large_x >= 0 and 5 >= large_y >= 0 and 6 >= next_move_large_x >= 0 and 5 >= next_move_large_y >= 0:
                        #large_three is equal to the value on (next_move_large_y,next_move_large_x)
                        large_three = board_right_way[next_move_large_y][next_move_large_x]
                        #large_col = the row gravity says large_x is on
                        large_col = gravity(board_right_way, large_x)
                        #if the rows match and the large_three has no chips back is give these value
                        if large_col == large_y and large_three == 0:
                            back = (large_y, large_x)

    return back


#checks for 3 in a row in the numpy array and and tries to make it 4 in a row
def four_in_a_row(board, chip):
    #defines board_right_way
    board_right_way = flip_board(board)
    #sets the default value back to be (-1 , -1)
    back = (-1 , -1)
#checks for 3 in a row vertically and looks for 4 in a row    
    #iterates through a initial box of values in the array
    for x in range(7):
        for y in range(4):
            #checks for 3 in a row vertically each x and y value given from above
            if board[y][x] == chip and board[y+1][x] == chip and board[y+2][x] == chip:
                #position of the connect 4 chip upwards
                large_y = 5-(y+3)
                #position of the connect 4 chip downwards
                small_y = 5-(y-1)
                
                #checking that the large_y will fit on the board
                if large_y <= 5:
                    #large_col = the row gravity says x is on
                    large_col = gravity(board_right_way, x)
                    #if the rows match back is give these value
                    if large_col == large_y:
                        back = (y,x)
                        
                #checking that the small_y will fit on the board
                if small_y >= 0:
                    #small_col = the row gravity says x is on
                    small_col = gravity(board_right_way, x)
                    #if the rows match back is give these value
                    if small_col == small_y:
                        back = (y,x)

#checks for 3 in a row horizontal and looks for 4 in a row
    #if back has not already been set
    if back == (-1, -1):
        #iterates through a initial box of values in the array
        for y in range(6):
            for x in range(5):
                #checks for 3 in a row horizontal each x and y value given from above
                if board[y][x] == chip and board[y][x+1] == chip and board[y][x+2] == chip:
                    #position of the connect 4 chip right
                    large_x = x+3
                    #position of the connect 4 chip left
                    small_x = x-1
                    #to account for position of origin
                    y = 5-(y)

                    #checking that the small_x will fit on the board
                    if small_x >= 0:
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match back is give these value
                        if small_col == y:
                            back = (y, small_x)
                    #checking that the large_x will fit on the board
                    if large_x <= 6:
                        #large_col = the row gravity says large_x is on
                        large_col = gravity(board_right_way, large_x)
                        #if the rows match back is give these value
                        if large_col == y:
                            back = (y, large_x)

                #can fill in 4 in a row in the middle
                #iterates through a initial box of values in the array
                if x <= 3:
                    #iterates from 1 to 2 and runs for each
                    for add_num in range(2):
                        add_num += 1
                        #checks for 3 in a row horizontal each x and y value given from above in the middle
                        if board[y][x] == chip and board[y][x+add_num] == chip and board[y][x+3] == chip:    
                            #to account for position of origin
                            y = 5-(y)
                            #if the filled in space is one the counter should go in the other
                            if add_num == 1:
                                middle_x = x+2
                            else:
                                middle_x = x+1
                            
                            #checking that the middle_x will fit on the board
                            if middle_x <= 6:
                                #middle_col = the row gravity says middle_x is on
                                middle_col = gravity(board_right_way, middle_x)
                                #if the rows match back is give these value
                                if middle_col == y:
                                    back = (y, middle_x)

#checks for 3 in a row in a positively diagonals and looks for 4 in a row
    #if back has not already been set          
    if back == (-1, -1):
        #iterates through a initial box of values in the array
        for y in range(4):
            for x in range(5):
                #checks for 3 in a row in a positively diagonals from each x and y value given from above
                if board[y][x] == chip and board[y+1][x+1] == chip and board[y+2][x+2] == chip:
                    #position of the connect 4 chip right
                    large_y = 5-(y+3)
                    #position of the connect 4 chip upwards
                    large_x = x+3
                    #position of the connect 4 chip left
                    small_y = 5-(y-1)
                    #position of the connect 4 chip downwards
                    small_x = x-1
                    
                    #checking that the small_x and small_y will fit on the board
                    if small_x >= 0 and small_y >= 0:
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match back is give these value
                        if small_col == small_y:
                            back = (small_y, small_x)
                    
                    #checking that the large_x and large_y will fit on the board
                    if large_x <= 6 and large_y <= 6:
                        #large_col = the row gravity says large_x is on
                        large_col = gravity(board_right_way, large_x)
                        #if the rows match back is give these value
                        if large_col == large_y:
                            back = (large_y, large_x)
                
                #can fill in 4 in a row in the middle
                #iterates through a initial box of values in the array
                if y <= 2 and x <= 3:
                    #iterates from 1 to 2 and runs for each
                    for add_num in range(2):
                        add_num += 1
                        #checks for 3 in a row positively diagonal each x and y value given from above in the middle
                        if board[y][x] == chip and board[y+add_num][x+add_num] == chip and board[y+3][x+3] == chip:    
                            #If the filled-in space is one, the counter should go in the other, and occupying the other axis.
                            if add_num == 1:
                                middle_x = x+2
                                middle_y = 5-(y+2)
                            else:
                                middle_x = x+1
                                middle_y = 5-(y+1)
                            
                            #checking that the middle_x will fit on the board
                            if middle_x <= 6 and middle_y <= 5:
                                #middle_col = the row gravity says middle_x is on
                                middle_col = gravity(board_right_way, middle_x)
                                #if the rows match back is give these value
                                if middle_col == middle_y:
                                    back = (middle_y, middle_x)

#checks for 3 in a row in a negative diagonals and looks for 4 in a row
    #if back has not already been set
    if back == (-1, -1):
        #iterates through a initial box of values in the array
        for y in range(4):
            y+=2
            for x in range(5):
                #checks for 3 in a row in a negative diagonal from each x and y value given from above
                if board[y][x] == chip and board[y-1][x+1] == chip and board[y-2][x+2] == chip:
                    #If the filled-in space is one, the counter should go in the other, and occupying the other axis."
                    large_y = 5-(y-3)
                    large_x = x+3
                    small_y = 5-(y+1)
                    small_x = x-1
                    #checking that the small_x and small_y will fit on the board
                    if small_x >= 0 and small_y >= 0:
                        #small_col = the row gravity says small_x is on
                        small_col = gravity(board_right_way, small_x)
                        #if the rows match back is give these value
                        if small_col == small_y:
                            back = (small_y, small_x)
                    #checking that the large_x and large_y will fit on the board
                    if large_x <= 6 and large_y <= 6:
                        #large_col = the row gravity says large_x is on
                        large_col = gravity(board_right_way, large_x)
                        #if the rows match back is give these value
                        if large_col == large_y:
                            back = (large_y, large_x)
                
                #can fill in 4 in a row in the middle
                #iterates through a initial box of values in the array
                if y >= 3 and x <= 3:
                    #iterates from 1 to 2 and runs for each
                    for add_num in range(2):
                        add_num += 1
                        #checks for 3 in a row negative diagonal each x and y value given from above in the middle
                        if board[y][x] == chip and board[y-add_num][x+add_num] == chip and board[y-3][x+3] == chip:    
                            #If the filled-in space is one, the counter should go in the other, and occupying the other axis."
                            if add_num == 1:
                                middle_x = x+2
                                middle_y = 5-(y-2)
                            else:
                                middle_x = x+1
                                middle_y = 5-(y-1)
                            #checking that the middle_x will fit on the board
                            if middle_x <= 6 and middle_y <= 5:
                                #middle_col = the row gravity says middle_x is on
                                middle_col = gravity(board_right_way, middle_x)
                                #if the rows match back is give these value
                                if middle_col == middle_y:
                                    back = (middle_y, middle_x) 
       
    return back


#looks for wins
def win(board, chip):
#looks for vertical wins
    win_chip = "\x1b[32m●\x1b[0m"
    #iterates through a initial box of values in the array
    for x in range(7):
        for y in range(3):
            #checks for 4 in a row vertically each x and y value given from above
            if board[y][x] == chip and board[y+1][x] == chip and board[y+2][x] == chip and board[y+3][x] == chip:
                #if won colour the wining chips green and return False
                for add_minus in range(4):
                    front_board[y+add_minus][x] = win_chip
                return False

#looks for horizontal wins
    #iterates through a initial box of values in the array
    for y in range(6):
        for x in range(4):
            #checks for 4 in a row horizontal each x and y value given from above
            if board[y][x] == chip and board[y][x+1] == chip and board[y][x+2] == chip and board[y][x+3] == chip:
                #if won colour the wining chips green and return False
                for add_minus in range(4):
                    front_board[y][x+add_minus] = win_chip
                return False

#looks for positively diagonal wins
    #iterates through a initial box of values in the array
    for y in range(3):
        for x in range(4):
            #checks for 4 in a row positively diagonals each x and y value given from above
            if board[y][x] == chip and board[y+1][x+1] == chip and board[y+2][x+2] == chip and board[y+3][x+3] == chip:
                #if won colour the wining chips green and return False
                for add_minus in range(4):
                    front_board[y+add_minus][x+add_minus] = win_chip
                return False

#looks for negative diagonal wins
    #iterates through a initial box of values in the array
    for y in range(3):
        y+=3
        for x in range(4):
            #checks for 4 in a row negative diagonals each x and y value given from above
            if board[y][x] == chip and board[y-1][x+1] == chip and board[y-2][x+2] == chip and board[y-3][x+3] == chip:
                #if won colour the winning chips green and return False
                for add_minus in range(4):
                    front_board[y-add_minus][x+add_minus] = win_chip
                return False


#prints out a front_end board
def front_end():
    # Create a new table
    table = PrettyTable()
    
    #picks out the 0 1 2 from the board_right_way (backend) and puts the correct characters on the front_board
    for y in range(7):
        for x in range(6):
            if board_right_way[x][y] == 0:
                front_board[x][y] = " "
            elif board_right_way[x][y] == 1:
                front_board[x][y] = "\x1b[33m●\x1b[0m"
            elif board_right_way[x][y] == 2:
                front_board[x][y] = "\x1b[31m●\x1b[0m"

    #if all_zero = False
    win(board_right_way,chip)        
              
    # Add the rows of the board_right_way to the table
    for row in front_board:
        table.add_row(row)

    # Set the alignment of the elements to center
    table.align = "c"

    # Set the border characters of the table
    table.border = True
    table.hrules = HRuleStyle.ALL
    table.vrules = VRuleStyle.ALL

    # Prints the table and the number underneath
    print(table.get_string(header=False))
    print("  1   2   3   4   5   6   7")


#take in human moves and checks if they are possible
def human_moves(user, chip, turn):
    #initialize valid_input as False
    valid_input = False
    #loops until a valid_input is given
    while valid_input == False:
        #gets a choice from the user
        column = user_clean_data(user, 7, 1)
        #sets show to true meaning that the  front end board will be shown
        show = True
        #check the user input column is not filled
        if column_unfilled(board, column):
            #finds the row it would fall to
            row = gravity(board, column)
            #inserts the chip in the board
            board[row][column] = chip
            #calls front_end which prints the board
            front_end()
            #check if this results in a win or draw
            win_draw = check_win_draw(show)
            #defines some values
            Game_in_progress = win_draw[0]
            game_outcome = win_draw[1]
            turn+=1
            valid_input = True
            #find good option in using the function possible_good_options
            four_good_options = possible_good_options(chip)
            four_move_def = four_good_options[0]
            three_move_def  = four_good_options[1]
            four_move  = four_good_options[2]
            three_move = four_good_options[3]
            
            #decides if the move is a attack, defense or neutral move
            if four_move_def[1] == column or three_move_def[1] == column:
                attack_defense_neutral = 1
            elif four_move[1] == column or three_move[1] == column:
                attack_defense_neutral = 3
            else:
                attack_defense_neutral = 2
            return (Game_in_progress,turn,game_outcome,row,column,attack_defense_neutral)
        
        else:
            # if the column is filled print this in red and check if there is a win or draw
            print("\x1b[1m\x1b[31mThis column is filled try another column\x1b[0m\x1b[0m")
            win_draw = check_win_draw(show)
            Game_in_progress = win_draw[0]
            game_outcome = win_draw[1]


#returns possible good options
def possible_good_options(chip):
    #picks the opposite chip and there attack is the opposite chips defense
    if chip == 1:
        chip = 2
        four_move_def = four_in_a_row(board_right_way, chip)
        three_move_def = three_in_a_row(board_right_way, chip)
        chip = 1
    else:
        chip = 1
        four_move_def = four_in_a_row(board_right_way, chip)
        three_move_def = three_in_a_row(board_right_way, chip)
        chip = 2
    #get the attack options
    four_move = four_in_a_row(board_right_way, chip)
    three_move = three_in_a_row(board_right_way, chip)
        
    return(four_move_def,three_move_def,four_move,three_move)


#the computers randomized good moves
def random_good_moves(user, chip, turn, show , forbidden_column , max_turn , Default_probability):
    #gets the 4 good decisions
    four_good_options = possible_good_options(chip)
    four_move_def = four_good_options[0]
    three_move_def  = four_good_options[1]
    four_move  = four_good_options[2]
    three_move = four_good_options[3]
    #the first for normal games and second for Testing hypotheses and changing parameters option 4
    if Default_probability:
        probability_list = [900,950,970,990]
    else:
        probability_list = [500,600,700,800]
    #random number for picking a move type
    probability_of_outcome = ra.randint(0,1000)
    #initializes attack_defense_neutral and got_output
    attack_defense_neutral = 0
    got_output = False
    
    #does a three in a row attack
    #checks if a output has already being got
    if got_output == False:
        #uses the random number to decide to do this or not
        if probability_of_outcome < probability_list[0]:
            #checks of four_move has a valid output
            if four_move[1] >= 0:
                #puts column = four_move column's recommendation
                column = four_move[1]
                #if the column is not the forbidden_column used for Testing hypotheses and changing parameters 1 and 2
                if column != forbidden_column:
                    #if the column is unfilled get the row and put the chip in the board
                    if column_unfilled(board, column):
                        row = gravity(board, column)
                        board[row][column] = chip
                        #if showing the board use for single player and multiplayer game print the last turn and the board
                        if show:
                            print(user,"Player picked",column+1)
                            front_end()
                        #check for wins and draws
                        win_draw = check_win_draw(show)
                        Game_in_progress = win_draw[0]
                        game_outcome = win_draw[1]
                        #if the forbidden_column is in use or max_turn (a function input)
                        if forbidden_column > -1  or max_turn == 30:
                            #if turn are equal to max turns stop the game a make it a draw
                            if turn == max_turn:
                                game_outcome = 0
                                Game_in_progress = False
                        #make got_output = True so that it will not be replayed further down make attack_defense_neutral = 3 meaning attack add 1 to turn as one turn is complete
                        got_output = True
                        attack_defense_neutral = 3
                        turn+=1
                        
    #does a three in a row defense
    #checks if a output has already being got            
    if got_output == False:
        #uses the random number to decide to do this or not
        if probability_of_outcome < probability_list[1]:
            #checks of four_move_def has a valid output
            if four_move_def[1] >= 0:
                #puts column = four_move_def's column recommendation
                column = four_move_def[1]
                #if the column is not the forbidden_column used for Testing hypotheses and changing parameters 1 and 2
                if column != forbidden_column:
                    #if the column is unfilled get the row and put the chip in the board
                    if column_unfilled(board, column):
                        row = gravity(board, column)
                        board[row][column] = chip
                        #if showing the board use for single player and multiplayer game print the last turn and the board
                        if show:
                            print(user,"Player picked",column+1)
                            front_end()
                        #check for wins and draws
                        win_draw = check_win_draw(show)
                        Game_in_progress = win_draw[0]
                        game_outcome = win_draw[1]
                        #if the forbidden_column is in use or max_turn (a function input)
                        if forbidden_column > -1  or max_turn == 30:
                            #if turn are equal to max turns stop the game a make it a draw
                            if turn == max_turn:
                                game_outcome = 0
                                Game_in_progress = False
                        #make got_output = True so that it will not be replayed further down make attack_defense_neutral = 3 meaning attack add 1 to turn as one turn is complete
                        got_output = True
                        attack_defense_neutral = 1
                        turn+=1

    #does a two in a row defense
    #checks if a output has already being got
    if got_output == False:
        #uses the random number to decide to do this or not
        if probability_of_outcome < probability_list[2]:
            #checks of three_move_def has a valid output
            if three_move_def[1] >= 0:
                #puts column = four_move_def's column recommendation
                column = three_move_def[1]
                #if the column is not the forbidden_column used for Testing hypotheses and changing parameters 1 and 2
                if column != forbidden_column:
                    #if the column is unfilled get the row and put the chip in the board
                    if column_unfilled(board, column):
                        row = gravity(board, column)
                        board[row][column] = chip
                        #if showing the board use for single player and multiplayer game print the last turn and the board
                        if show:
                            print(user,"Player picked",column+1)
                            front_end()
                        #check for wins and draws
                        win_draw = check_win_draw(show)
                        Game_in_progress = win_draw[0]
                        game_outcome = win_draw[1]
                        #if the forbidden_column is in use or max_turn (a function input)
                        if forbidden_column > -1  or max_turn == 30:
                            #if turn are equal to max turns stop the game a make it a draw
                            if turn == max_turn:
                                game_outcome = 0
                                Game_in_progress = False
                        #make got_output = True so that it will not be replayed further down make attack_defense_neutral = 3 meaning attack add 1 to turn as one turn is complete
                        got_output = True
                        attack_defense_neutral = 1
                        turn+=1

    #does a two in a row attack
    #checks if a output has already being got
    if got_output == False:
        #uses the random number to decide to do this or not
        if probability_of_outcome < probability_list[3]:
            #checks of three_move has a valid output
            if three_move[1] >= 0:
                #puts column = four_move_def's column recommendation
                column = three_move[1]
                #if the column is not the forbidden_column used for Testing hypotheses and changing parameters 1 and 2
                if column != forbidden_column:
                    #if the column is unfilled get the row and put the chip in the board
                    if column_unfilled(board, column):
                        row = gravity(board, column)
                        board[row][column] = chip
                        #if showing the board use for single player and multiplayer game print the last turn and the board
                        if show:
                            print(user,"Player picked",column+1)
                            front_end()
                        #check for wins and draws
                        win_draw = check_win_draw(show)
                        Game_in_progress = win_draw[0]
                        game_outcome = win_draw[1]
                        #if the forbidden_column is in use or max_turn (a function input)
                        if forbidden_column > -1  or max_turn == 30:
                            #if turn are equal to max turns stop the game a make it a draw
                            if turn == max_turn:
                                game_outcome = 0
                                Game_in_progress = False
                        #make got_output = True so that it will not be replayed further down make attack_defense_neutral = 3 meaning attack add 1 to turn as one turn is complete
                        got_output = True
                        attack_defense_neutral = 3
                        turn+=1

    #checks if a output has already being got
    if got_output == False:            
        #initializes pick_again
        pick_again = True
        #a loop to insure a eventual output
        while pick_again:
            #picks a random column
            column = ra.randint(0,6)
            #if the column is not the forbidden_column used for Testing hypotheses and changing parameters 1 and 2
            if column != forbidden_column:
                #if the column is unfilled get the row and put the chip in the board
                if column_unfilled(board, column):
                    row = gravity(board, column)
                    board[row][column] = chip
                    #if showing the board use for single player and multiplayer game print the last turn and the board
                    if show:
                        print(user,"Player picked",column+1)
                        front_end()
                    #check for wins and draws
                    win_draw = check_win_draw(show)
                    Game_in_progress = win_draw[0]
                    game_outcome = win_draw[1]
                    #if the forbidden_column is in use or max_turn (a function input)
                    if forbidden_column > -1  or max_turn == 30:
                        #if turn are equal to max turns stop the game a make it a draw
                        if turn == max_turn:
                            game_outcome = 0
                            Game_in_progress = False
                    #make got_output = True so that it will not be replayed further down make attack_defense_neutral = 3 meaning attack add 1 to turn as one turn is complete
                    got_output = True
                    attack_defense_neutral = 2
                    turn+=1
                    pick_again = False
                
    return (Game_in_progress,turn,game_outcome,row,column,attack_defense_neutral)


#checks for wins or draw outputs the chip winner if there is one changes Game_in_progress
def check_win_draw(show):
    #initialized values
    game_end = -1
    Game_in_progress = True
    #if its a draw make Game_in_progress = False finishing the game and game_end = 0 representing a draw
    if draw(board_right_way):
        Game_in_progress = False
        game_end = 0
        #show is true print Draw
        if show:
            print("Draw")
    #if its a win make Game_in_progress = False finishing the game and the chip representing the winner
    elif win(board_right_way,chip) == False:
        Game_in_progress = False
        game_end = chip
        #show is true print the use colour and Player won
        if show:
            print(user + " Player won")
    #if the game is finish return Game_in_progress == False and the game_end (0,1 or 2)
    if Game_in_progress == False: 
        win_draw_status = False, game_end
        return win_draw_status
    #else return Game_in_progress == true and the game_end = -1
    else:
        win_draw_status = True, game_end
        return win_draw_status

#the first board that is printed in single player and multiplayer
def blank_front_end_board():
    # Create a new table
    table = PrettyTable()
    # fill the grid with black spaces
    for y in range(7):
            for x in range(6):
                front_board[x][y] = " "

    # Add the rows of the board_right_way to the table
    for row in front_board:
            table.add_row(row)
    
    # Set the alignment of the elements to center
    table.align = "c"

    # Set the border characters of the table
    table.border = True
    table.hrules = HRuleStyle.ALL
    table.vrules = VRuleStyle.ALL

    # Print the table
    print(table.get_string(header=False))
    print("  1   2   3   4   5   6   7")


#the play again menu that is use multiple times
def play_again(game_type):
    #takes a user input then makes it lower case
    replay_input = input("Replay? Input y or n: ")
    lower = replay_input.lower()
    #while the inputs are not n or y stays in the loop
    while lower != "n" and lower != "y":
        #prints Input Invalid in red
        print("\x1b[1m\x1b[31mInput Invalid\x1b[0m\x1b[0m")
        #takes a user input then makes it lower case again
        replay_input = input("Replay? Input y or n: ")
        lower = replay_input.lower()
    #if the input is n return False and the users input from the selection menu with is called from the function selection
    if lower == "n":
        game_type = selection(csv_count_rows(False) > 2, False)
        return (False,game_type)
    #else if the input is y return y and the game type brought in to this function
    else:
        return (True,game_type)


#the main menu for the game 
def selection(csv_row_num,first_run):
    #check is it is a first turn
    if not first_run:
        print()
    #prints a red number and the then a option
    print("Pick one of the following using the numbers adjacent:")
    print("\x1b[1m\x1b[31m1\x1b[0m\x1b[0m = Simulation")
    print("\x1b[1m\x1b[31m2\x1b[0m\x1b[0m = Single player")
    print("\x1b[1m\x1b[31m3\x1b[0m\x1b[0m = Multiplayer")
    print("\x1b[1m\x1b[31m4\x1b[0m\x1b[0m = Testing hypotheses and changing parameters")
    #if the number of csv rows is sufficient print Statistics normally and give the user a chose of 1-5
    if csv_row_num:
        print("\x1b[1m\x1b[31m5\x1b[0m\x1b[0m = Statistics")
        game_type = user_clean_data("", 5, 1)
    #if the number of csv rows is insufficient print Statistics grayed out and a warning and give the user a chose of 1-4
    else:
        print("\x1b[90m5 = Statistics\x1b[0m (This is not possible correct data not present play games or simulations first)")
        game_type = user_clean_data("", 4, 1)
    #return the users input (the game type)
    return game_type


#calculates percentages
def percentage_calculator(input_list):
    #initialise counts
    counts = [0,0,0]
    #gets the length of the input list
    total = len(input_list)
    #iterates through the input_list and -1 from the number to get the index in count then add 1 to that index position
    for n in input_list:
        counts[n - 1] += 1
    #initialise percentages
    percentages = []
    #if the number in input_list is greater that 0 reinitialize percentages
    if total > 0:
        percentages = []
        # in the loop get the percentage for each place in the counts list then append this to the percentages and return this
        for count in counts:
            percentage = (count/total)*100
            percentages.append(percentage)
    return percentages       
 
#collects data each turn of the game
def during_game_stats_collection(values_back,turn):
    # if the remainder when dividing turns by two is 0 the (yellow player)
    if turn % 2 == 0:
        #all the values taken in from values_back are appended to lists for the duration of the simulation or several games
        row_y = values_back[3] + 1
        column_y = values_back[4] + 1
        atk_def_neutral_y = values_back[5]
        column_y_list.append(column_y)
        row_y_list.append(row_y)
        atk_def_neutral_list_y.append(atk_def_neutral_y)
    #red player data
    else:
        #all the values taken in from values_back are appended to lists for the duration of the simulation or several games
        row_r = values_back[3] + 1
        column_r = values_back[4] + 1
        atk_def_neutral_r = values_back[5]
        column_r_list.append(column_r)
        row_r_list.append(row_r)
        atk_def_neutral_list_r.append(atk_def_neutral_r)
    #Game_in_progress and turn are given values from values_back
    Game_in_progress = values_back[0]
    turn = values_back[1]
    return (column_y_list , row_y_list , column_r_list , row_r_list , games_outcomes , atk_def_neutral_list_y , atk_def_neutral_list_r, Game_in_progress, turn)


#compiling the data after each game
def after_game_stats_compiling(values_back,during_game_stats):
    #gets the mean yellow column and appends it to a list
    mean_y_col = round(statistics.mean(during_game_stats[0]),2)
    all_mean_y_col.append(mean_y_col)
    #gets the mean yellow row and appends it to a list
    mean_y_row = round(statistics.mean(during_game_stats[1]),2)
    all_mean_y_row.append(mean_y_row)
    #gets the mean red column and appends it to a list
    mean_r_col = round(statistics.mean(during_game_stats[2]),2)
    all_mean_r_col.append(mean_r_col)
    #gets the mean red row and appends it to a list
    mean_r_row = round(statistics.mean(during_game_stats[3]),2)
    all_mean_r_row.append(mean_r_row)
    #get the percentage attack defense and neutral from the percentage_calculator for yellow and red
    percentage_atk_def_n_y = percentage_calculator(atk_def_neutral_list_y)
    percentage_atk_def_n_r = percentage_calculator(atk_def_neutral_list_r)
    #gets the number  of turns and appends it to a list
    turn = during_game_stats[8]
    turn_list.append(turn)
    #appends percentage attack defense and neutral for yellow and red to there respective lists
    pct_atk_def_n_list_y.append(percentage_atk_def_n_y)
    pct_atk_def_n_list_r.append(percentage_atk_def_n_r)
    #gets game_outcome from values_back and appends it to a list
    game_outcome = values_back[2]
    game_outcome_list.append(game_outcome)
    #return several values
    return (pct_atk_def_n_list_y , pct_atk_def_n_list_r, game_outcome_list , all_mean_y_col , all_mean_y_row , all_mean_r_col , all_mean_r_row,turn_list)


#prepares data for csv and adds it to the csv
def prep_data_for_csv(game_stats_lists,num_games,game_type):
    #takes data in from game_stats_lists
    pct_atk_def_n_list_y = game_stats_lists[0]
    pct_atk_def_n_list_r = game_stats_lists[1]
    game_outcome_list = game_stats_lists[2]
    all_mean_y_col = game_stats_lists[3]
    all_mean_y_row = game_stats_lists[4]
    all_mean_r_col = game_stats_lists[5]
    all_mean_r_row = game_stats_lists[6]
    turn_list = game_stats_lists[7]
    #for each game on these list it does the following process
    for game in range (num_games):
        #initialise row to []
        row = []
        #outcome is given the value of the game_outcome_list for the game the loop is on
        outcome = game_outcome_list[game]
        #if the outcome is 0 append Draw, 1 append Win or 2 append Lose
        if outcome == 0:
            row.append("Draw")
        elif outcome == 1:
            row.append("Win")
        else:
            row.append("Lose")
        #append the the mean of yellow and red rows and columns and pct_atk_def_n_separated_y/r = is the pct_atk_def_n_list_y/r from each game
        row.append(all_mean_y_col[game])
        row.append(all_mean_y_row[game])
        row.append(all_mean_r_col[game])
        row.append(all_mean_r_row[game])
        pct_atk_def_n_separated_y = pct_atk_def_n_list_y[game]
        pct_atk_def_n_separated_r = pct_atk_def_n_list_r[game]
        #separates out attack defense and neutral and adds a % sign to it this is done for yellow and red
        for move_type in range (3):
            row.append(str(pct_atk_def_n_separated_y[move_type])+"%")
        for move_type in range (3):
            row.append(str(pct_atk_def_n_separated_r[move_type])+"%")
        #check the game_type and appends the right string respectively
        row.append(turn_list[game])
        if game_type == 0:
            row.append("Sim")
        elif game_type == 1:
            row.append("Single")
        elif game_type == 2:
            row.append("Multi")
        elif game_type == 3:
            row.append("Hyp")
        else:
            row.append("Base")
        #calls a function to append the data
        csv_appending(row)
    #empties the lists to avoid duplicates
    emptying_lists_after_stored()
    
#count rows in csv file and insure it exists
def csv_count_rows(hyp_or_base):
    #initialise at -1 to the account of header
    count = -1
    #if the file exists open and read
    if os.path.exists("database.csv"):
        with open("database.csv") as x:
            csv_read = csv.reader(x)
            for row in csv_read:
                #if the function argument hyp_or_base is False
                if hyp_or_base == False:
                    #for each row without Hyp or Base in the position 12 to the right add 1 to count
                    if (row[12]) != "Hyp" and (row[12]) != "Base":
                        count += 1
                #else if hyp_or_base is not False add 1 to count for every row
                else:
                        count += 1
    #return count
    return count


#appends rows to the csv file
def csv_appending(row):
    #if the file exists open and append the rows of data
    if os.path.exists("database.csv"):
        with open('database.csv', 'a', newline='') as x:
            write = csv.writer(x)
            write.writerow(row)
    #if the file doesn't exist open, append the headers and then append the rows of data
    else:
        with open('database.csv', 'a', newline='') as x:
            write = csv.writer(x)
            write.writerow(["win_lose","y_col","y_row","r_col","r_row","y_def","y_n","y_atk","r_def","r_n","r_atk","turn","g_type"])
            write.writerow(row)


#empties lists after each game
def emptying_lists():
    column_y_list.clear()
    column_r_list.clear()
    row_y_list.clear()
    row_r_list.clear()
    atk_def_neutral_list_y.clear()
    atk_def_neutral_list_r.clear()


#empties lists after data is putin the csv file
def emptying_lists_after_stored():
    pct_atk_def_n_list_y.clear()
    pct_atk_def_n_list_r.clear()
    game_outcome_list.clear()
    all_mean_y_col.clear()
    all_mean_y_row.clear()
    all_mean_r_col.clear()
    all_mean_r_row.clear()
    turn_list.clear()


#empties lists before stats can be performed to avoid cross contamination of data
def csv_list_clear():
    win_lose_draw.clear()
    y_cols.clear()
    y_rows.clear()
    r_cols.clear()
    r_rows.clear()
    defense_y.clear()
    defense_r.clear()
    neutral_y.clear()
    neutral_r.clear()
    attack_y.clear()
    attack_r.clear()
    turns_csv.clear()
    game_types.clear()
    mean_median_mode_list.clear()
    percentage_win_draw_lose.clear()
    percentage_atk_n_def_y.clear()
    percentage_atk_n_def_r.clear()
    win_draw_lose.clear()
    atk_n_def_y.clear()
    atk_n_def_r.clear()
    

#empties lists before testing hypotheses and changing parameters can be tested
def base_hyp_lists_clear():
    percentage_win_draw_lose_base_hyp.clear()
    percentage_win_draw_lose_base.clear()
    percentage_atk_n_def_y_base.clear()
    percentage_atk_n_def_r_base.clear()
    percentage_win_draw_lose_hyp.clear()
    percentage_atk_n_def_y_hyp.clear()
    percentage_atk_n_def_r_hyp.clear()
    

#graphs data input
def graph(input_1,input_2,input_3,input_4,names_num,stats_type,hyp):
    #if the argument hyp is False meaning these are statistics the following will be run
    if hyp == False:
        #defines x_axis
        x_axis = np.arange(names_num)
        #if the user picked option 1
        if stats_type == 0:
            #defines several values
            outcome_labels = ["Yellow Columns","Yellow Rows","Red Columns","Red Rows"]
            mean  = [input_1[0],input_2[0],input_3[0],input_4[0]]
            median  = [input_1[1],input_2[1],input_3[1],input_4[1]]
            mode  = [input_1[2],input_2[2],input_3[2],input_4[2]]
            #makes the bars on the bar chart
            plt.bar(x_axis -0.3, mean, width=0.3, label = "Mean")
            plt.bar(x_axis +0, median, width=0.3, label = "Median")
            plt.bar(x_axis +0.3, mode, width=0.3, label = "Mode")
            #labels along the x axis
            plt.xticks(x_axis, outcome_labels)
            #labels the y axis
            plt.ylabel("Average Move")
            #adds a title
            plt.title("Average Columns and Rows")
            #adds a legend
            plt.legend()
        #if the user picked option 2
        elif stats_type == 1:
            #defines several values
            outcome_labels = ["Yellow Win" , "Red Win" , "Draw"]
            colours = ["#FFFF00", "#FF0000" , "#F5F5DC"]
            #makes the pie chart
            plt.pie(input_1, labels = outcome_labels , colors = colours , autopct = "%1.1f%%")
            #adds a title
            plt.title("Win Lose Draw")
        #if the user picked option 3
        elif stats_type == 2:
            #defines several values
            outcome_labels = ["Attack" , "Neutral" , "defense"]
            #makes the pie chart
            plt.pie(input_2, labels = outcome_labels , autopct = "%1.1f%%")
            #adds a title
            plt.title("Yellow Attack, Neutral and Defensive Moves")
        #if the user picked option 4    
        elif stats_type == 3:
            #defines several values
            outcome_labels = ["Attack" , "Neutral" , "defense"]
            #makes the pie chart
            plt.pie(input_3, labels = outcome_labels , autopct = "%1.1f%%")
            #makes the pie chart
            plt.title("Red Attack, Neutral and Defensive Moves")
            #adds a title
    #if the argument hyp is True meaning these are Testing hypotheses and changing parameters the following will be run
    else:
        #defines x_axis
        x_axis = np.arange(names_num)
        #defines several values
        outer_colors = ["#FFFF00" , "#FF0000" , "#D5D6CA"]
        inner_colors = ["#FCFF98" , "#FF6060" , "#EFEFE7"]
        outcome_labels = ["Yellow Win" , "Red Win" , "Draw"]
        outer_outcome_labels = ["Yellow Win Base" , "Red Win Base" , "Draw Base"]
        inner_outcome_labels = ["Yellow Win Modified" , "Red Win Modified" , "Draw Modified"]
        #makes the bars on the bar chart
        plt.bar(x_axis -0.15, input_1 , width=0.3, label = "base" , color = outer_colors)
        plt.bar(x_axis +0.15, input_2 , width=0.3, label = "hyp", color = inner_colors)
        #labels along the x axis
        plt.xticks(x_axis, outcome_labels)
        #labels the y axis
        plt.ylabel("Average Move")
        #adds a title
        plt.title("Base (Darker) Vs After Modification (Lighter)")
        #adds percentages above the bars on the chart
        for num in range(len(input_1)):
            plt.text(num - 0.15 , int(round(float(input_1[num])) + 1) , str(round(float(input_1[num]))) + "%", ha = "center")
        for num in range(len(input_2)):
            plt.text(num + 0.15 , int(round(float(input_2[num])) + 1) , str(round(float(input_2[num]))) + "%", ha = "center")
        #defines lists
        outer_patches = []
        inner_patches = []
        #prepare data for the legend
        for i in range(len(outer_colors)):
            color_outer = outer_colors[i]
            color_inner = inner_colors[i]
            label_outer = outer_outcome_labels[i]
            label_inner = inner_outcome_labels[i]
            patch_outer = mpatches.Patch(color = color_outer, label = label_outer)
            patch_inner = mpatches.Patch(color = color_inner, label = label_inner)
            outer_patches.append(patch_outer)
            inner_patches.append(patch_inner)
        #orders the data for the legend
        legend_data = [outer_patches[0], inner_patches[0], outer_patches[1], inner_patches[1], outer_patches[2], inner_patches[2]]
        #adds a legend
        plt.legend(handles = legend_data , loc = "best")
        #makes a max height for the chart
        plt.ylim(0, 100)
    #shows the pie chart or bar chart
    plt.show()


#counts up data from the csv for graphing
def count_csv(win_count,lose_count,draw_count,row):
    #adds to the relevant variable for win draw lose
    if (row[0]) == "Win":
        win_count += 1
    elif (row[0]) == "Lose":
        lose_count += 1
    else:
        draw_count += 1
    #append the percentage for attack defense and neutral for yellow and red to lists after striping off the % sign
    defense_y.append(float((row[5]).rstrip('%')))
    neutral_y.append(float((row[6]).rstrip('%')))
    attack_y.append(float((row[7]).rstrip('%')))
    defense_r.append(float((row[8]).rstrip('%')))
    neutral_r.append(float((row[9]).rstrip('%')))
    attack_r.append(float((row[10]).rstrip('%')))
    #appends yellow and red columns and rows to lists
    y_cols.append(float(row[1]))
    y_rows.append(float(row[2]))
    r_cols.append(float(row[3]))
    r_rows.append(float(row[4]))
    #appends turns to a list
    turns_csv.append(float(row[11]))
    #returns the 3 variables
    return (win_count,lose_count,draw_count)


#gets the mean median mode of values that come in and returns the values
def mean_median_mode(input_list):
    mean_value = statistics.mean(input_list)
    median_value = statistics.median(input_list)
    mode_value = statistics.mode(input_list)
    return (mean_value , median_value, mode_value)


#does statistics on the data to make it graphable
def stats(hypotheses_base , hypotheses , num_hyp_tests):
    #initialize variables
    win_count = 0
    lose_count = 0
    draw_count = 0
    both_lists_calculated = False
    #clears lists
    csv_list_clear()
    #opens the csv file and goes to the first line with relevant data
    with open ("database.csv") as csv_file:
        dataFrame = csv.reader(csv_file, delimiter = ",")
        next(dataFrame)
        #if the argument hypotheses is False it skips the row that are Hyp and Base data
        if hypotheses == False:
            for row in dataFrame:
                if (row[12]) != "Hyp" and (row[12]) != "Base":
                    #this adds to the row if it is True
                    counts_out = count_csv(win_count,lose_count,draw_count,row)
                    win_count = counts_out[0]
                    lose_count = counts_out[1]
                    draw_count = counts_out[2]
            #puts last 3 variables in a list
            win_draw_lose = [win_count , lose_count , draw_count]
            #gets the mean for attack, neutral and defense for yellow and red and puts them in lists
            atk_n_def_y = [(mean_median_mode(attack_y)[0]) , (mean_median_mode(neutral_y)[0]) , (mean_median_mode(defense_y)[0])]
            atk_n_def_r = [(mean_median_mode(attack_r)[0]) , (mean_median_mode(neutral_r)[0]) , (mean_median_mode(defense_r)[0])]
            #adds up the lists and assigns them to the respective variable
            win_draw_lose_total = sum(win_draw_lose)
            atk_n_def_y_total = sum(atk_n_def_y)
            atk_n_def_r_total = sum(atk_n_def_r)
            #gets the overall percentages
            for list_position in range (3):
                percentage_win_draw_lose.append(win_draw_lose[list_position]/win_draw_lose_total*100)
                percentage_atk_n_def_y.append((atk_n_def_y[list_position])/atk_n_def_y_total*100)
                percentage_atk_n_def_r.append((atk_n_def_r[list_position])/atk_n_def_r_total*100)
            #graph menu and user choice
            print()
            print("Pick one of the following using the numbers adjacent:")
            print("\x1b[32m1\x1b[0m = Red and yellow average columns and rows")
            print("\x1b[32m2\x1b[0m = Red and yellow wins and draws")
            print("\x1b[32m3\x1b[0m = Yellow attack, defense and neutral moves")
            print("\x1b[32m4\x1b[0m = Red attack, defense and neutral moves")
            stats_type = user_clean_data("", 4, 1)
            #if the user picked 1 calls the graph function with the following arguments
            if stats_type == 0:
                graph(mean_median_mode(y_cols),mean_median_mode(y_rows),mean_median_mode(r_cols),mean_median_mode(r_rows),4,stats_type , False)
            #if the use didn't pick 1 calls the graph function with the following arguments
            else:
                graph(percentage_win_draw_lose , percentage_atk_n_def_y , percentage_atk_n_def_r , 0 , 3 , stats_type , False)
        #if hypotheses is true
        elif hypotheses:
            #counts rows and find the row to start reading data from sets rows_read to 0
            num_rows = csv_count_rows(True)
            start_row = num_rows - (num_hyp_tests)
            with open ("database.csv") as csv_file:
                dataFrame = csv.reader(csv_file, delimiter = ",")
                for i in range(start_row):
                    next(dataFrame)
                row = next(dataFrame)
                rows_read = 0
                #if rows_read is not = to the argument num_hyp_tests count the wins draws and loses and add one to rows_read
                for row in dataFrame:
                    if rows_read != num_hyp_tests:
                        counts_out = count_csv(win_count,lose_count,draw_count,row)
                        win_count = counts_out[0]
                        lose_count = counts_out[1]
                        draw_count = counts_out[2]
                        rows_read += 1
                #puts last 3 variables in a list
                win_draw_lose = [win_count , lose_count , draw_count]
                 #adds up the list
                win_draw_lose_total = sum(win_draw_lose)
                #gets the overall percentages
                for list_position in range (3):
                    percentage_win_draw_lose.append(win_draw_lose[list_position]/win_draw_lose_total*100)
                #a shallow copy is made meaning the original list before the change this is then appended to the list percentage_win_draw_lose_base_hyp
                percentage_win_draw_lose_copy = percentage_win_draw_lose.copy()
                percentage_win_draw_lose_base_hyp.append(percentage_win_draw_lose_copy)
                #if the length of the list is 2 the graph function is called with the arguments shown
                if len(percentage_win_draw_lose_base_hyp) == 2:
                    percentage_win_draw_lose_base = percentage_win_draw_lose_base_hyp[0]
                    percentage_win_draw_lose_hyp = percentage_win_draw_lose_base_hyp[1]
                    graph(percentage_win_draw_lose_base,percentage_win_draw_lose_hyp,0,0,3,0, True)
            #if testing hypotheses and changing parameters data collection is complete clear these lists
            if hypotheses_base == 1:
                base_hyp_lists_clear()
                

#to estimate time taken necessary for the simulations
def time_estimate(games_played):
    #when games played is 10 get the timestamp then gets time for ten games by taking end time from start time
    if games_played == 10:
        end_time_ten = time.time()
        ten_time = end_time_ten - start_time
        #gets the multiplayer which is the number ten games time needs to be multiplied by to the estimate time then this round estimated time and print it
        multiplayer = num_simulation/games_played
        estimate_time = multiplayer * ten_time
        estimate_time = round(estimate_time)           
        print("Estimated time = "+ str(estimate_time) +"s")


#initializes values for task_not_done
task_not_done = True
#starts with menu
game_type = selection(csv_count_rows(False) > 2,True)


#while task_not_done means the program runs indefinitely
while(task_not_done):
    #if the user picked 1
    if game_type == 0:
        #replay is set to true
        replay = True
        #while replay is true
        while replay:
            #ask for a number of simulations set games_played to 0 and set start time
            num_simulation = user_clean_data("", 1000, 100)
            #num_simulation = 5
            games_played = 0
            start_time = time.time()
            #while num_simulation is not = to games_played emptying the lists add 1 to games_played make a board and make a flipped board then set the 3 variables
            while num_simulation != games_played:
                emptying_lists()
                games_played+= 1
                board = make_board()
                board_right_way = flip_board(board)
                turn = 0
                Game_in_progress = True
                show = False
                #while the game is in progress check if turns divided by 2's remainder is 0 if it is sets user to \x1b[33m●\x1b[0m and chip to 1 and call the function random_good_moves
                while Game_in_progress:
                    if turn % 2 == 0:
                        user = "\x1b[33m●\x1b[0m"
                        chip = 1
                        values_back = random_good_moves(user, chip, turn, show, -1 , 35 , True)
                    #check if turns divided by 2's remainder is 1 if it is sets user to \x1b[31m●\x1b[0m and chip to 2 and call the function random_good_moves
                    else:
                        user = "\x1b[31m●\x1b[0m"
                        chip = 2
                        values_back = random_good_moves(user, chip, turn, show, -1 , 35 , True)
                    #call the function during_game_stats_collection to collect data set the values of Game_in_progress and turn
                    during_game_stats = during_game_stats_collection(values_back,turn)
                    Game_in_progress = during_game_stats[7]
                    turn = during_game_stats[8]
                #calls the time_estimate function to estimate the time taken
                time_estimate(games_played)
                #complies stats after the game
                game_stats_lists = after_game_stats_compiling(values_back,during_game_stats)
            #prepares data for the csv file and adds it
            prep_data_for_csv(game_stats_lists,num_simulation,game_type)
            #calls the play_again function and gets outputs
            play_again_statues = play_again(game_type)
            replay = play_again_statues[0]
            game_type = play_again_statues[1]

    #if the user picked 2
    elif game_type == 1:
        #replay is set to true
        replay = True
        #while replay is true
        while replay:
            #emptying the lists make a board and make a flipped board then set the 2 variables
            emptying_lists()
            board = make_board()
            board_right_way = flip_board(board)
            blank_front_end_board()
            turn = 0
            Game_in_progress = True
            #while the game is in progress check if turns divided by 2's remainder is 0 if it is sets user to \x1b[33m●\x1b[0m and chip to 1 and call the function random_good_moves
            while Game_in_progress:
                if turn % 2 == 0:
                    user = "\x1b[33m●\x1b[0m"
                    chip = 1
                    values_back = human_moves(user, chip, turn)
                #check if turns divided by 2's remainder is 1 if it is sets user to \x1b[31m●\x1b[0m and chip to 2 and call the function random_good_moves
                else:   
                    show = True
                    user = "\x1b[31m●\x1b[0m"
                    chip = 2
                    values_back = random_good_moves(user, chip, turn, show, -1 , 35 , True)
                #call the function during_game_stats_collection to collect data set the values of Game_in_progress and turn                    
                during_game_stats = during_game_stats_collection(values_back,turn)
                Game_in_progress = during_game_stats[7]
                turn = during_game_stats[8]
            #complies stats after the game and prepares data for the csv file and adds it
            game_stats_lists = after_game_stats_compiling(values_back,during_game_stats)
            prep_data_for_csv(game_stats_lists,1,game_type)
            #calls the play_again function and gets outputs
            play_again_statues = play_again(game_type)
            replay = play_again_statues[0]
            game_type = play_again_statues[1]
    
    #if the user picked 3
    elif game_type == 2:
        #replay is set to true
        replay = True
        #while replay is true
        while replay:
            #emptying the lists make a board and make a flipped board then set the 2 variables
            board = make_board()
            board_right_way = flip_board(board)
            blank_front_end_board()
            turn = 0
            Game_in_progress = True
            #while the game is in progress check if turns divided by 2's remainder is 0 if it is sets user \x1b[33m●\x1b[0m and chip to 1 and call the function random_good_moves
            while Game_in_progress:
                if turn % 2 == 0:
                    user = "\x1b[33m●\x1b[0m"
                    chip = 1
                    values_back = human_moves(user, chip, turn)
                #check if turns divided by 2's remainder is 1 if it is sets user to \x1b[31m●\x1b[0m and chip to 2 and call the function random_good_moves
                else:
                    user = "\x1b[31m●\x1b[0m"
                    chip = 2
                    values_back = human_moves(user, chip, turn)
                #call the function during_game_stats_collection to collect data set the values of Game_in_progress and turn
                during_game_stats = during_game_stats_collection(values_back,turn)
                Game_in_progress = during_game_stats[7]
                turn = during_game_stats[8]
            #complies stats after the game and prepares data for the csv file and adds it
            game_stats_lists = after_game_stats_compiling(values_back,during_game_stats)
            prep_data_for_csv(game_stats_lists,1,game_type)
            #calls the play_again function and gets outputs
            play_again_statues = play_again(game_type)
            replay = play_again_statues[0]
            game_type = play_again_statues[1]
    
    #if the user picked 4
    elif game_type == 3:
        #replay is set to true
        replay = True
        #while replay is true prints all these options and gives the user the choice to pick one
        while replay:
            print()
            print("Pick one of the following using the numbers adjacent:")
            print("\x1b[32m1\x1b[0m = What if column 3 (one to the left of the middle column) is blocked off?")
            print("\x1b[32m2\x1b[0m = What if the grid size is reduced from 7x6 to 6x6?")
            print("\x1b[32m3\x1b[0m = What if there is a cap of 30 turns, above this is a draw?")
            print("\x1b[32m4\x1b[0m = What if the players are less likely to make good moves?")
            modification = user_clean_data("", 4, 1)
            #runs twice once in base mode then in modified mode
            for run in range (2):
                #sets num_simulation to 100, games_played to 0 and gets start time
                num_simulation = 100
                games_played = 0
                start_time = time.time()
                #if a base run the variables below apply
                if run == 0:
                    max_turn = 35
                    forbidden_column = -1
                    Default_probability = True
                #if run is 2
                else:
                    #if the user picked 1 set forbidden_column = 2
                    if modification == 0:
                        forbidden_column = 2
                    #if the user picked 2 set forbidden_column = 0
                    elif modification == 1:
                        forbidden_column = 0
                    #if the user picked 3 set max_turn to 30
                    elif modification == 2:
                        max_turn = 30
                    #if the user picked 4 change from Default_probabilities by setting Default_probability = False
                    else:
                        Default_probability = False
                #while num_simulation is not = to games_played emptying the lists add 1 to games_played make a board and make a flipped board then set the 3 variables
                while num_simulation != games_played:
                    emptying_lists()
                    games_played+= 1
                    board = make_board()
                    board_right_way = flip_board(board)
                    turn = 0
                    Game_in_progress = True
                    show = False
                    #while the game is in progress check if turns divided by 2's remainder is 0 if it is sets user to \x1b[33m●\x1b[0m and chip to 1 and call the function random_good_moves
                    while Game_in_progress:
                        if turn % 2 == 0:
                            user = "\x1b[33m●\x1b[0m"
                            chip = 1
                            values_back = random_good_moves(user, chip, turn, show , forbidden_column , max_turn , Default_probability)
                        #check if turns divided by 2's remainder is 1 if it is sets user to \x1b[31m●\x1b[0m and chip to 2 and call the function random_good_moves
                        else:
                            user = "\x1b[31m●\x1b[0m"
                            chip = 2
                            values_back = random_good_moves(user, chip, turn, show , forbidden_column , max_turn , Default_probability)
                        #call the function during_game_stats_collection to collect data set the values of Game_in_progress and turn
                        during_game_stats = during_game_stats_collection(values_back,turn)
                        Game_in_progress = during_game_stats[7]
                        turn = during_game_stats[8]
                    #complies stats after the game and prepares data for the csv file and adds it
                    game_stats_lists = after_game_stats_compiling(values_back,during_game_stats)
                #if it is the base run call prep_data_for_csv with the arguments shown
                if run == 0:
                    prep_data_for_csv(game_stats_lists,num_simulation,4)
                #if it is the modified run call prep_data_for_csv with the arguments shown
                else:
                    prep_data_for_csv(game_stats_lists,num_simulation,game_type)
                #calls stats to get a graph
                stats(run , True , num_simulation)
            #calls the play_again function and gets outputs
            play_again_statues = play_again(game_type)
            replay = play_again_statues[0]
            game_type = play_again_statues[1]
    
    #if the user picked 5
    elif game_type == 4:
        #replay is set to true
        replay = True
        #while replay is true call stats which will ask the user for there preferred graph type
        while replay:
            stats(0,False,0)
            #calls the play_again function and gets outputs
            play_again_statues = play_again(game_type)
            replay = play_again_statues[0]
            game_type = play_again_statues[1]