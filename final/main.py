# implement templates workshop

from flask import Flask, render_template, jsonify, request
from game_engine import *
from components import *
from mp_game_engine import *
from flask_game_engine import *
# Try ensure there are no variables of like names, namespace
# "importing * not great practice"

app = Flask(__name__)

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface(ships, board_size = 10):
    if request.methods == "GET":
        return render_template('placement.html', ships , board_size)
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Received'}), 200
    
@app.route('/', methods=['GET'])
def root(main_render_file = 'main.html',player_board ):
    # place the ships on the board
    # current_ board = placement(player_board, data)
    # return render_template(main_render_file, current_boad)
    
@app.route('/attack', methods=['GET'])
def process_attack():
    x = request.args.get('x')
    y = request.args.get('y')
    # process input - return hit or miss
    # return AI attack
    # check if game is finished - inform user


if __name__ == "__main__":
    app.run()