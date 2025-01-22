# Game Engine
from art import *
import textwrap
from components import *
from tabulate import tabulate
import time

def parser(input):
    if input.strip().lower() == 'q':
      return 'q'

    x,y = input.replace(' ', '').replace('(','').replace(')','').split(',')
    coordinates = int(x), int(y)
    return coordinates

def cli_coordinates_input(board_size = 10):
    ### attempt to create quitting option
    example_list = [[None]*board_size for _ in range(board_size)] 
    while True:
        try:
            coord_str = input("Input attack coordinate or quit (q), only plain x,y format accepted: ") # or quit (q)

            coords = parser(coord_str)
            if coords == 'q':
                return 'q'
            
            example_list[coords[0]][coords[1]]
            return coords
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...") 
        except IndexError:
            print("Oops, that value is out of range. Try another!")
    

def attack(coordinates, board, battleships):
    a = board[coordinates[0]][coordinates[1]]
    if a != None: # HIT!
        battleships[a] = int(battleships[a]) - 1
        board[coordinates[0]][coordinates[1]] = None

        return True
    
    else: # MISS!
        return False

def check(battleships):
    return all(i == 0 for i in battleships.values())

def display_board(grid_board):
    print(grid_board,"\n","_"*150,"\n")
    time.sleep(0.2)

def simple_game_loop():
    active = True

    # Welcome title 
    title = text2art("Battleships")
    print(f"\nWeclome to \n{textwrap.indent(title, "           ")}...please zoom out")

    board_size = 10
    battleships = create_battleships() 
    board = initialise_board()
    board_w_ships = place_battleships(board, battleships)
    grid_board = tabulate(board_w_ships, tablefmt="grid")
    print(grid_board,"\n","_"*150,"\n")

    while active == True:
        coordinates = cli_coordinates_input(board_size) # _quit_input
        if coordinates == 'q':
          print("Quitting the game...")
          active = False
          break

        result = attack(coordinates,board_w_ships,battleships)
        if result == True:
            print("HIT!\n")
        if result == False:
            print("MISS!\n")
        
        grid_board = tabulate(board_w_ships, tablefmt="grid")
        display_board(grid_board)
        
        if check(battleships) == True:
            print("GAME OVER") # maybe make in fancy textart
            command = input(f"Play again?: (y/n)\n ")
            command = command.strip()

            if command == 'y':
                simple_game_loop()
            if command == 'n':
                active = False

if __name__ == '__main__':
    simple_game_loop()