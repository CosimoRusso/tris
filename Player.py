from Node import Node
import shelve


class Player:
    def __init__(self, tris):
        self.tris = tris
        self.root = Node(tris, None)
        self.create_tree()
        self.position = self.root

    def create_tree(self):
        root = self.root
        if root.tris.whose_turn() == 'x':
            self.Vmax(root, -1e6, 1e6)
        else:
            self.Vmin(root, -1e6, 1e6)

    def Vmax(self, node, alpha, beta):
        if node.finished():
            return node.calculate_minimax()
        v = -1
        for action in node.actions():
            child = node.result(action)
            v = max([v, self.Vmin(child, alpha, beta)])
            if v >= beta:
                node.minimax = v
                return v
            alpha = max([alpha, v])
        node.minimax = v
        return v

    def Vmin(self, node, alpha, beta):
        if node.finished():
            return node.calculate_minimax()
        v = 1
        for action in node.actions():
            child = node.result(action)
            v = min([v, self.Vmax(child, alpha, beta)])
            if v >= beta:
                node.minimax = v
                return v
            alpha = min([alpha, v])
        node.minimax = v
        return v

    def move(self):
        out = None
        max_minimax = -1
        for child in self.position.children:
            if child.minimax > max_minimax:
                out = child
                max_minimax = child.minimax
                self.change_position(child)
        return out.move

    def opponent_move(self, move):
        for child in self.position.children:
            if move == child.move:
                self.change_position(child)
                return
        raise Exception("This move was not in my tree, consider yourself the winner. And please contact the developer because it's a bug")

    def change_position(self, node):
        self.position = node
