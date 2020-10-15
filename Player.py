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
            d[self.tris.whose_turn()] = self.root
        else:
            self.root = tree
            self.root.tris = tris
        self.position = self.root

    def read_tree(self):
        d = shelve.open("tree")
        try:
            data = d[self.tris.whose_turn()]
        except Exception as e:
            print(e)
            data = False
        if not data:
            print("No data found on disk, building tree with CPU...")
        else:
            print("Reading data from disk")
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
        self.calculate_minimax(root)

    def calculate_minimax(self, node):
        if node.minimax is not None:
            return node.minimax
        elif node.tris.whose_turn() == 'x':
            node.minimax = max([self.calculate_minimax(n) for n in node.children])
        else:
            node.minimax = min([self.calculate_minimax(n) for n in node.children])
        return node.minimax

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
