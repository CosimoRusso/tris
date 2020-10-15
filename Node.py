from copy import deepcopy


class Node:
    def __init__(self, tris, parent):
        self.tris = tris
        self.parent = parent
        self.minimax = None
        self.children = []
        self.move = None

    def player(self):
        """Return 'x' or 'o'"""
        return self.tris.whose_turn()

    def actions(self):
        """Returns all the possible actions for the tris game in the form 'x:int'"""
        return self.tris.get_possible_moves()

    def result(self, move):
        """Given a move in the form of an integer returns a new Node whose tris is the actual (deepcopied) tree with the move done"""
        tris = deepcopy(self.tris)
        tris.put(move)
        n = Node(tris, self)
        n.move = move
        self.children.append(n)
        return n

    def finished(self):
        """Return True if the game is finished, False otherwise"""
        return self.tris.finished()

    def utility(self, player):
        """Takes a player in the form 'x' or 'o' and returns its utility if it's a final state. Otherwise throw error"""
        assert self.tris.finished()
        if self.tris.get_winner() == player:
            return 1
        elif self.tris.get_winner() is None:
            return 0
        else:
            return -1

    def calculate_minimax(self):
        if self.finished():
            u = self.utility('x')
            self.minimax = u
            return u
        elif self.player() == 'x':
            self.minimax = max([n.minimax for n in self.children])
        else:
            self.minimax = min([n.minimax for n in self.children])

