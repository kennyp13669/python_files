####################################################################
# This program is a minesweeper clone. The user must make selections
# and press enter each time.
#
# Modify GRIDSIZE to play a different size field.
#
# Modify CHANCE to allocate more bombs
#
# Created by Kenny Peel on 9/1/2021
####################################################################
import random
GRIDSIZE = [10, 12] # x, y. 
field = [[0 for i in range(GRIDSIZE[0])] for j in range(GRIDSIZE[1])]
check_vector = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
win_lose = 2 # 0 win, 1 lose, 2 playing
bomb_count = 0
total_squares = GRIDSIZE[0] * GRIDSIZE[1]
exit_game = 0
state = 0
CHANCE = .8

class squares:
    def __init__(self, bomb, relationship, revealed, flagged):
        self.bomb = bomb
        self.relationship = relationship
        self.revealed = revealed
        self.flagged = flagged

def gameloop():
    global exit_game
    global state
    global win_lose
    while exit_game == 0:
        if(state == 0): # Decision
            print("Check a square ------- 1")
            print("Flag a square  ------- 2")
            check = input("Make a selection: ") # 1 = check, 2 = flag
            while(int(check) != 1 and int(check) != 2):
                print("please enter a valid selection")
                check = input("Make a selection: ")
            coordinates = [0, 0]
            coordinates[0] = input("Please enter an x coordinate (column): ")
            coordinates[1] = input("Please enter a y coordinate (row): ")
            while(int(coordinates[0]) < 0 or
                  int(coordinates[1]) < 0 or
                  int(coordinates[0]) > GRIDSIZE[0] or
                  int(coordinates[1]) > GRIDSIZE[1]):
                print("please enter a valid selection")
                coordinates[0] = input("Please enter an x coordinate (column): ")
                coordinates[1] = input("Please enter a y coordinate (row): ")
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            coordinates[0] -= 1
            coordinates[1] = GRIDSIZE[1] - coordinates[1]        
            if(int(check) == 1):
                # show the square
                field[coordinates[1]][coordinates[0]].revealed = 1
                state = 1
            else:
                # toggle flag
                field[coordinates[1]][coordinates[0]].flagged = not field[coordinates[1]][coordinates[0]].flagged
                state = 0
                printFunction()
                
        elif(state == 1): # Check square
            if(field[coordinates[1]][coordinates[0]].bomb == 1):
                win_lose = 1
                state = 3
            else:
                autoReveal()
                state = 2

        elif(state == 2): # Still playing
            revealed_count = 0
            # each row
            for y in range(0, GRIDSIZE[1]):
                # each square in the row
                for x in range(0, GRIDSIZE[0]):
                    # is revealed
                    if field[y][x].revealed == 1:
                        revealed_count += 1
            if(revealed_count == (total_squares - bomb_count)):
                win_lose = 0 #win
                state = 3
            else:
                state = 0
            printFunction()
            
        elif(state == 3): # End game
            exit_game = 1
            if(win_lose == 0):
                printFunction()
                print("You win!")
            else:
                losePrintFunction()
                print("Nice try, better luck next time.. haha what next time!?")
    
def printFunction():
    for y in range(0, GRIDSIZE[1]):
        # print x coordinates
        if((GRIDSIZE[1] - y) < 10):
            print(GRIDSIZE[1] - y, " ", end = "")
        else:
            print(GRIDSIZE[1] - y, end = "")
            print(" ", end = "")
        # print the stuff in each cell of one row
        for x in range(0, GRIDSIZE[0]):
            print("[", end = "")
            decideWhatToPrint(y, x)
            print("]", end = "")
        # newline
        print("")
    # print the y coordinates
    print("    ", end = "")
    for y in range(1, GRIDSIZE[0] + 1):
        if(y < 10):
            print(y, " ", end = "")
        else:
            print(y, end = "")
            print(" ", end = "")
    print("")

def losePrintFunction():
    for y in range(0, GRIDSIZE[1]):
        # print x coordinates
        if((GRIDSIZE[1] - y) < 10):
            print(GRIDSIZE[1] - y, " ", end = "")
        else:
            print(GRIDSIZE[1] - y, end = "")
            print(" ", end = "")
        # print the stuff in each cell of one row
        for x in range(0, GRIDSIZE[0]):
            print("[", end = "")
            loseDecideWhatToPrint(y, x)
            print("]", end = "")
        print("")
    # print the y coordinates
    print("    ", end = "")
    for y in range(1, GRIDSIZE[0] + 1):
        if(y < 10):
            print(y, " ", end = "")
        else:
            print(y, end = "")
            print(" ", end = "")
    print("")

def bombAllocation():
    for y in range(0, GRIDSIZE[1]):
        for x in range(0, GRIDSIZE[0]):
            if(random.random() > CHANCE):
                global bomb_count
                bomb_count += 1
                field[y][x] = squares(1, 0, 0, 0)
            else:
                field[y][x] = squares(0, 0, 0, 0)

def decideWhatToPrint(y, x):
    if(field[y][x].revealed == 0):
        if((field[y][x]).flagged == 1):
            print(">", end = "")
        else:
            print(".", end = "")
    else:
        if((field[y][x]).relationship == 0):
            print(" ", end = "")
        else:
            print(field[y][x].relationship, end = "")

def loseDecideWhatToPrint(y, x):
    if((field[y][x]).bomb):
        print("#", end = "")
    else:
        if(field[y][x].revealed == 0):
            print(".", end = "")
        else:
            if((field[y][x]).relationship == 0):
                print(" ", end = "")
            else:
                print(field[y][x].relationship, end = "")
    
def relationships():
    # each row
    for y in range(0, GRIDSIZE[1]):
        # each square in the row
        for x in range(0, GRIDSIZE[0]):
            # is not a bomb
            if field[y][x].bomb == 0:
                bombs_touching = 0
                # each check location
                for z in range(0, len(check_vector)):
                    # if it's on the field
                    if((x + check_vector[z][0] >= 0) and
                       (x + check_vector[z][0] <= GRIDSIZE[0]-1) and
                       (y + check_vector[z][1] >= 0) and
                       (y + check_vector[z][1] <= GRIDSIZE[1]-1)):
                        if(field[y + check_vector[z][1]][x + check_vector[z][0]].bomb == 1):
                           bombs_touching += 1
                field[y][x].relationship = bombs_touching

def autoReveal():
    # For each square, if it's not a bomb and not revealed, 
    #   check all the ones around it.
    #   If one of them is (not a bomb and revealed and zero),
    #       then reveal the square that you checked around.
    #       and do the loop again
    #global checked_squares
    keep_going = 1
    while(keep_going == 1):
        keep_going = 0
        # each row
        for y in range(0, GRIDSIZE[1]):
            # each square in the row
            for x in range(0, GRIDSIZE[0]):
                # is not a bomb and revealed and zero
                if((field[y][x].bomb == 0) and (field[y][x].revealed == 0)):
                    # each check location
                    for z in range(0, len(check_vector)):
                        # if it's on the field
                        if((x + check_vector[z][0] >= 0) and
                           (x + check_vector[z][0] <= GRIDSIZE[0]-1) and
                           (y + check_vector[z][1] >= 0) and
                           (y + check_vector[z][1] <= GRIDSIZE[1]-1)):
                            # if (not a bomb and revealed and zero)
                            if((field[y + check_vector[z][1]][x + check_vector[z][0]].bomb == 0) and
                               (field[y + check_vector[z][1]][x + check_vector[z][0]].revealed == 1) and
                               (field[y + check_vector[z][1]][x + check_vector[z][0]].relationship == 0)):
                                keep_going = 1
                                field[y][x].revealed = 1

def main():
    bombAllocation()
    relationships()
    #losePrintFunction()
    printFunction()
    gameloop()    
                
main()
