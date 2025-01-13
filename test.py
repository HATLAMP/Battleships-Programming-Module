#test
import components
import game_engine
from tabulate import tabulate

print(type(components.initialise_board(10)))

a = components.create_battleships()
print(type(a))

b = components.initialise_board(10)

#print(tabulate(components.place_battleships(b,a), tablefmt= 'grid'))

# print(tabulate(components.place_battleships(b,a,'random'), tablefmt= 'grid'))
a = components.place_battleships(b,a, 'custom')
print(tabulate(a, tablefmt='grid'))


