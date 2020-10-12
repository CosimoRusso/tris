import numpy as np


class Tris:
    def __init__(self):
        self.turn = True  # x starts
        self.game = np.array([[None for _ in range(3)] for _ in range(3)])
        self.winner = None
        self.moves = 0

    def finished(self):
        return self.moves == 9 or self.winner is not None

    def put(self, pos):
        (x, y) = pos
        assert self.game[x, y] is None
        assert 0 <= x < 3 and 0 <= y < 3
        self.game[x, y] = self.turn
        self.moves += 1
        self.check_winner(pos)
        self.change_turn()

    def check_winner(self, pos):
        (x, y) = pos
        row = self.game[x, :]
        col = self.game[:, y]
        if row[0] == row[1] == row[2]:
            self.winner = row[0]
            return True
        elif col[0] == col[1] == col[2]:
            self.winner = col[0]
            return True
        elif x == y:
            diag = [self.game[i, i] for i in range(3)]
            if diag[0] == diag[1] == diag[2]:
                self.winner = diag[0]
                return True
        counter_diag = [(0, 2), (1, 1), (2, 0)]
        if pos in counter_diag:
            list = [self.game[i, j] for (i, j) in counter_diag]
            if list[0] == list[1] == list[2]:
                self.winner = list[0]
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
        out = []
        for x in range(3):
            for y in range(3):
                if self.game[x, y] is None:
                    out.append((x, y))
        return out

    def __str__(self):
        out = ""
        for y in range(3):
            for x in range(3):
                c = self.game[x, y]
                if c is None:
                    out += " "
                elif c is True:
                    out += "x"
                else:
                    out += "o"
                out += " | "
            out = out[0:len(out)-3]
            out += "\n"
        return out
