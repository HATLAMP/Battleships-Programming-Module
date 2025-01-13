# Multiplayer Game Engine
import random
from components import *
from art import *
import textwrap
from components import *
from tabulate import tabulate
from game_engine import *

players = {'user' : [None,None] , 'ai': [None,None]}

def generate_attack(board_size):
    x = random.randint(0,board_size-1)
    y = random.randint(0,board_size-1)
    coordinates_attack = x,y
    return coordinates_attack

def place_knowledge(coordinates, ai_board_copy):
    coord_attack = parser(coordinates)
    ai_board_copy[coord_attack[0]][coord_attack[1]]


def ai_opponent_game_loop():
    active = True

    # Welcome title 
    title = text2art("Battleships")
    print(f"\nWeclome to \n{textwrap.indent(title, "           ")}...please zoom out")

    # Initialise boards
    board_size = 10
    brd1 = initialise_board(board_size)
    brd2 = initialise_board(board_size)
    brd2_user_copy = initialise_board(board_size) 

    # Initialise battleships
    btlshp1 = create_battleships()
    btlshp2 = create_battleships()
    players["user"][1] = btlshp1
    players["ai"][1] = btlshp2

    # Place ships
    brd1_w_ships = place_battleships(brd1, btlshp1, 'custom')
    brd2_w_ships = place_battleships(brd2, btlshp2, 'random')

    players["user"][0] = brd1_w_ships 
    players["ai"][0] = brd2_w_ships

    # Display board
    if active == True:
        grid_board = tabulate(brd1_w_ships, tablefmt="grid")
        print("Your Board")
        print(grid_board,"\n","_"*150,"\n")

    # Game loop
    while active == True:
        ## USER play
        # User attack coordinates
        coordinates1 = cli_coordinates_input(board_size)
        if coordinates1 == 'q':
          print("Quitting the game...")
          active = False
          break

        # Result of user attack and user knowledge board update
        result_user = attack(coordinates1,brd2_w_ships,btlshp2)
        if result_user == True:
            print("Opponents Board\nHIT!\n")
            brd2_user_copy[coordinates1[0]][coordinates1[1]] = 'X'
        if result_user == False:
            print("Opponents Board\nMISS!\n")
            brd2_user_copy[coordinates1[0]][coordinates1[1]] = '~'

        # display of what user knows
        grid_board_ai_data = tabulate(brd2_user_copy, tablefmt="grid")
        display_board(grid_board_ai_data)
        
        # Check if user has sunk all ai ships
        if check(btlshp2) == True:
            print("Congratulations, you won!!!!\nGAME OVER") # maybe make in fancy textart
            command = input(f"Play again?: (y/n)\n ")
            command = command.strip()

            if command == 'y':
                ai_opponent_game_loop()
            if command == 'n':
                active = False
        
        ## AI play
        coordinates2 = generate_attack(board_size)

        result_ai = attack(coordinates2,brd1_w_ships,btlshp1)
        if result_ai == True:
            print("AI attack\nYour Board\nHIT!\n")
        if result_ai == False:
            print("AI attack\nYour Board\nMISS!\n")
        
        # Display users board after ai attack
        grid_board_user = tabulate(brd1_w_ships, tablefmt="grid")
        display_board(grid_board_user)
        
        if check(btlshp1) == True:
            print("You lost!\nGAME OVER") # maybe make in fancy textart
            command = input(f"Play again?: (y/n)\n ")
            command = command.strip()

            if command == 'y':
                ai_opponent_game_loop()
            if command == 'n':
                active = False


if __name__ == '__main__':
    ai_opponent_game_loop()