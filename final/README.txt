README

Completed features:
components
- Required functions completed: initialise_board, create_battleships, place_battlships
- place_battlships includes 3 algorithms: 'simple','random', and 'custom'
game_engine
- Reguired functions completed: cli_coordinates_input, attack, simple_game_loop
- Aditional functions to support required functions: parser, check, display_board
mp_game_engine
- Reguired functions: generate_attack, ai_opponent_game_loop
- Function to support the display of the users previous guesses: place_knowledge
    This feature allows the user to see a display of a board which reveals whether a
    position on the ai opponents board has been guessed and what the result was.

Requirements:
- art must be installed, pip install art
- tabulate must be installed, pip install tabulate
- numpy must be installed, pip install numpy

