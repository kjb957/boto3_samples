"""Minesweeper program"""

import random

class Minesweep():
    """Game of Mine Sweeper"""
    def __init__(self, r=9, c=9, num_mines=10):
        self.r = r
        self.c = c
        self.rc = r * c
        self.num_mines = num_mines
        self.mine_grid = self.create_mine_grid()
        self.play_grid = ['_'] * (self.rc)

    def bounded(self, n, s_list):
        return [i for i in s_list if -1 < i < n ]

    def surrounding_points(self, p):
        l = p - self.c
        u = p + self.c
        if l % self.c == 0:
            s_p = [l, l + 1, p + 1, u, u + 1]
        elif l % self.c == self.c - 1 or l % self.c == -1:
            s_p = [l - 1, l, p - 1, u - 1, u]
        else:
            s_p = [l - 1, l, l + 1, p - 1, p + 1, u - 1, u, u + 1]
        return self.bounded(self.rc, s_p)

    def unchecked_surrounding_points(self, p):
        return [i for i in self.surrounding_points(p) if self.play_grid[i] == '_']

    def create_mine_grid(self):
        """create a flat list representing a grid of mines"""
        mine_grid = [0] * (self.rc)
        mine_positions = sorted(random.sample(range(self.rc), self.num_mines))
        for i in mine_positions:
            mine_grid[i] = 9
            s_p = self.surrounding_points(i)
            for j in s_p:
                if j not in mine_positions:
                    mine_grid[j] += 1
        return mine_grid

    def print_grid(self):
        for self.i in range(self.r):
            print(str(self.play_grid[self.i * self.c: self.i * self.c + self.c]) + '', "\t\t\t\t", self.mine_grid[self.i * self.c: self.i * self.c + self.c])

    def linear_coord(self, r, c):
        return r * self.c + c

    def check_for_mine(self, r, c):
        return self.check_square(self.linear_coord(r, c))

    def check_square(self, p):
        if self.mine_grid[p] == 9:
            return False
        else:
            if self.play_grid[p] == '_':
                val = self.mine_grid[p]
                self.play_grid[p] = val
                if val == 0:
                    for point in self.unchecked_surrounding_points(p):
                        self.check_square(point)
            return True

ms = Minesweep(12, 12, 10)

while True:
    print()
    ms.print_grid()
    r,c, *_ = input('Enter R C ').split()
    r = int(r); c = int(c)
    if not ms.check_for_mine(r, c):
        print('BOOM !!!!!')
        break



