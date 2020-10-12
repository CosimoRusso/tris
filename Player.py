from Node import Node
import shelve

class Player:
    def __init__(self, tris):
        self.tris = tris
        self.root = Node(tris, None)
        tree = self.read_tree()
        if not tree:
            self.create_tree()
            d = shelve.open("tree")
            d["tree"] = self.root
        else:
            self.root = tree
            self.root.tris = tris
        self.position = self.root

    def read_tree(self):
        d = shelve.open("tree")
        try:
            data = d["tree"]
        except Exception as e:
            print(e)
            data = False
        if not data:
            print("No data!")
        return data

    def create_tree(self):
        root = self.root
        frontier = [root]
        leaves = []
        while len(frontier) > 0:
            node = frontier.pop(0)
            if node.finished():
                node.calculate_minimax()
                leaves.append(node)
            else:
                for action in node.actions():
                    child = node.result(action)
                    frontier.append(child)
        for node in leaves:
            n = node
            while n.parent is not None:
                p = n.parent
                p.calculate_minimax()
                n = p

    def move(self):
        max_minimax = -1
        for child in self.position.children:
            if child.minimax > max_minimax:
                self.position = child
                max_minimax = child.minimax
        return self.position.move

    def opponent_move(self, move):
        for child in self.position.children:
            if child.move == move:
                self.position = child
