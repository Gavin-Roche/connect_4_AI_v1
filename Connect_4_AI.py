'''this is a program based around connect 4 the user can play simulation, single player and multiplayer game they
can also get graphs of the games and simulations finally they can do Testing hypotheses and changing parameters
to understand how these changes affect the games'''

#imports part of python's standard library
import random as ra

#takes in user inputs and validates they are acceptable inputs if not it will ask for the input again
def user_clean_data(user, upper_limit, lower_limit):
    # for getting the prompt to output to the user
    def get_prompt():
        #this is for the game itself picking the row
        if upper_limit == 7:
            return user + " Player input a number between " + str(lower_limit) + "-" + str(upper_limit) + ": "
        #this is for the menus options picking the menu there is 4 or 5 option in all the menus this can cater to both
        elif upper_limit == 2:
            return "Input a number between " + str(lower_limit) + "-" + str(upper_limit) + ": "

    while True:
        try:
            user_input = input(get_prompt())
            #this check that the number is a integer and is between between lower_limit and upper_limit if True it returns the value
            if (user_input.isnumeric() and lower_limit <= int(user_input) <= upper_limit):
                #turn the user_input into an integer and subtracts 1 as all background tasks start at 0 rather than 1
                user_input = int(user_input) - 1
                return user_input
            else:
                #prints: Input Invalid in red
                print("\x1b[1m\x1b[31mInput Invalid\x1b[0m\x1b[0m")
        
        # Exit the program gracefully if interrupted
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit()


# checks to see if the top row of the inputted column is full then return False if it is filled or True if it is not
def column_unfilled(board, column):
    return board[5][column] == 0


# finds the lowest row that is empty from the inputted column and returns that row
def gravity(board, column):
    for hole in range(6):
        if board[hole][column] == 0:
            return hole


# Makes a 6x7 board filled with 0s (integers)
def make_board():
    clean_board = [
        [0, 0, 0, 0, 0, 0, 0],  # row 0
        [0, 0, 0, 0, 0, 0, 0],  # row 1
        [0, 0, 0, 0, 0, 0, 0],  # row 2
        [0, 0, 0, 0, 0, 0, 0],  # row 3
        [0, 0, 0, 0, 0, 0, 0],  # row 4
        [0, 0, 0, 0, 0, 0, 0],  # row 5
    ]
    return clean_board
board = make_board()


# Makes a 6x7 board filled with None (for holding any Python objects)
def front_end_board():
    zero_board = [
        [None, None, None, None, None, None, None],  # row 0
        [None, None, None, None, None, None, None],  # row 1
        [None, None, None, None, None, None, None],  # row 2
        [None, None, None, None, None, None, None],  # row 3
        [None, None, None, None, None, None, None],  # row 4
        [None, None, None, None, None, None, None],  # row 5
    ]
    return zero_board
front_board = front_end_board()


# Flip the board vertically
def flip_board(board):
    flipped_board = board[::-1]  # reverse the rows
    return flipped_board
board_right_way = flip_board(board)


#checks if the board is a filled along the top row and if it is it returns True
def draw(board):
    for column in range(7):
        if board[0][column] == 0:
            return False
    return True


#checks for 2 in a row in the array and and tries to make it 3 in a row
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


#checks for 3 in a row in the array and and tries to make it 4 in a row
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
    num_zero = 0

    #picks out the 0 1 2 from the board_right_way (backend) and puts the correct characters on the front_board
    for y in range(7):
        for x in range(6):
            if board_right_way[x][y] == 0:
                front_board[x][y] = " "
                num_zero += 1
            elif board_right_way[x][y] == 1:
                front_board[x][y] = "\x1b[33m●\x1b[0m"
            elif board_right_way[x][y] == 2:
                front_board[x][y] = "\x1b[31m●\x1b[0m"

    if num_zero != 42:
        win(board_right_way,chip)  
              
    # Print the board manually
    horizontal_line = "+---" * 7 + "+"
    print(horizontal_line)
    for row in front_board:
        # This prints a row with '|' separators between cells
        print("| " + " | ".join(row) + " |")
        print(horizontal_line)

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
            
            return (Game_in_progress,turn,game_outcome,row,column)
        
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
                        #make got_output = True so that it will not be replayed further down
                        got_output = True
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
                        #make got_output = True so that it will not be replayed further down
                        got_output = True
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
                        #make got_output = True so that it will not be replayed further down
                        got_output = True
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
                        #make got_output = True so that it will not be replayed further down
                        got_output = True
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
                    #make got_output = True so that it will not be replayed further down make
                    got_output = True
                    turn+=1
                    pick_again = False
                
    return (Game_in_progress,turn,game_outcome,row,column)


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
        game_type = selection(False)
        return (False,game_type)
    #else if the input is y return y and the game type brought in to this function
    else:
        return (True,game_type)


#the main menu for the game 
def selection(first_run):
    #check is it is a first turn
    if not first_run:
        print()
    #prints a red number and the then a option
    print("Pick one of the following using the numbers adjacent:")
    print("\x1b[1m\x1b[31m1\x1b[0m\x1b[0m = Single player")
    print("\x1b[1m\x1b[31m2\x1b[0m\x1b[0m = Multiplayer")
    game_type = user_clean_data("", 2, 1)
    return game_type

#initializes values for task_not_done
task_not_done = True
#starts with menu
game_type = selection(True)


#while task_not_done means the program runs indefinitely
while(task_not_done):
    #if the user picked 1
    if game_type == 0:
        #replay is set to true
        replay = True
        #while replay is true
        while replay:
            board = make_board()
            board_right_way = flip_board(board)
            front_end()
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
                Game_in_progress = values_back[0]
                turn = values_back[1]
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
            board = make_board()
            board_right_way = flip_board(board)
            front_end()
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
                Game_in_progress = values_back[0]
                turn = values_back[1]
            #calls the play_again function and gets outputs
            play_again_statues = play_again(game_type)
            replay = play_again_statues[0]
            game_type = play_again_statues[1]