# Components
import numpy as np
from random import randint
from random import choice
import json

def initialise_board(size= 10):
    board = [[None]*size for _ in range(size)]
    return board

def create_battleships(filename = 'battleships.txt'):
    battileships = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        key, value = line.strip().split(':')
        battileships[key.strip()] = value.strip()
    return battileships

def commands():
    command = input("Input attack coordinate or quit (q), only plain x,y format accepted: ")
    return command

def place_battleships(board, ships, algorithm = 'simple'):
    keys = ships.keys() # list of names of ships
    values = ships.values() # list of lengths of ships
    board_w_ships = board[:]
    board_size = len(board)
    orientation_options = ['h','v']

    if algorithm == 'simple':
        row = 0
        for k,val in zip(keys, values):
            row = (row % len(ships))
            val = int(val)
            for column in range(val):
                board_w_ships[row][column] = k
            row += 1
        return board_w_ships
    
    if algorithm == 'random':
        for k,val in zip(keys, values):
            # Finding appropriate random points
            val = int(val)
            orientation = choice(orientation_options)

            find_placement = True
            while find_placement == True:
                x = randint(0, board_size - 1)
                y = randint(0, board_size - 1)

                if orientation == 'h' and x + val <= (board_size-1):
                    if all(board_w_ships[y][x+i] is None for i in range(val)):
                        find_placement = False
                if orientation == 'v' and y + val <= (board_size-1):
                    if all(board_w_ships[y + i][x] is None for i in range(val)):    
                        find_placement = False
                
            # Placing on board
            if orientation == 'h':
                for i in range(val):
                    board_w_ships[y][x+i] = k
            if orientation == 'v':
                for i in range(val):
                    board_w_ships[y+i][x] = k

        # Returning board with ships
        return board_w_ships
    
    if algorithm == 'custom':
        custom_placement = json.load(open('placement.json','r'))
        # returns items in value as str

        ## The following does not check if user has input correct values for the .json file
        for key,val in custom_placement.items(): # returns list of tupils of key-value pairs
            x = int(val[0])
            y = int(val[1])
            orientation = val[2]
            ship_length = int(ships[key])

            # Placing on board
            if orientation == 'h':
                for i in range(ship_length):
                    board_w_ships[y][x+i] = key
            if orientation == 'v':
                for i in range(ship_length):
                    board_w_ships[y+i][x] = key
        return board_w_ships


        
