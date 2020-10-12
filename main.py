from Tris import Tris
from Node import Node
from Player import Player
import re

tris = Tris()
root = Node(tris, None)

regex = re.compile(r'(\d) (\d)')


def play():
    print("Building tree. This might take a while...")
    player = Player(tris)
    print("Tree built!")
    while not tris.finished():
        if tris.whose_turn() == 'x':
            move = player.move()
            tris.put(move)
        else:
            coords = input("It's %s turn. Give me coords: " % tris.whose_turn())
            x = int(regex.search(coords).group(1))
            y = int(regex.search(coords).group(2))
            tris.put((x, y))
            player.opponent_move((x, y))
        print(tris)
        if tris.winner is not None:
            print("Winner: %s" % tris.get_winner())


play()

