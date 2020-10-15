from Tris import Tris
from Player import Player

tris = Tris()


def play():
    start = input("Do you want to start ([y]/n)?")
    if start == '' or start == 'y':
        tris.change_turn()
    print("Building tree. This might take a while...")
    player = Player(tris)
    print("Tree built!")
    print(tris)
    while not tris.finished():
        if tris.whose_turn() == 'x':
            move = player.move()
            tris.put(move)
        else:
            pos = input("It's %s turn. Give me coords: " % tris.whose_turn())
            x = int(pos)
            tris.put(x)
            player.opponent_move(x)
        print(tris)
    if tris.winner is not None:
        print("Winner: %s" % tris.get_winner())
    else:
        print("Draw, try again")


play()

