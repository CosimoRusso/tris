
class Tris:
    def __init__(self):
        self.turn = True  # x starts
        self.game = [None for _ in range(9)]
        self.winner = None
        self.moves = 0

    def finished(self):
        return self.moves == 9 or self.winner is not None

    def put(self, pos):
        assert self.game[pos] is None
        assert 0 <= pos < 9
        self.game[pos] = self.turn
        self.moves += 1
        self.check_winner()
        self.change_turn()

    def check_winner(self):
        positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for (x, y, z) in positions:
            if self.game[x] is not None and self.game[x] == self.game[y] == self.game[z]:
                self.winner = self.game[x]
                return True

    def change_turn(self):
        self.turn = not self.turn

    def whose_turn(self):
        """Returns 'x' or 'o'"""
        return 'x' if self.turn else 'o'

    def get_winner(self):
        if self.winner is True:
            return 'x'
        elif self.winner is False:
            return 'o'

    def get_possible_moves(self):
        return [i for (i, x) in enumerate(self.game) if x is None]

    def __str__(self):
        out = ""
        for x in range(9):
            c = self.game[x]
            if c is None:
                out += " "
            elif c is True:
                out += "x"
            else:
                out += "o"
            if (x + 1) % 3 == 0:
                out += "\t%d | %d | %d\n" % (x-2, x-1, x)
            else:
                out += " | "
        return out
