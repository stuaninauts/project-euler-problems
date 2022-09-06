#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 15
# https://github.com/stuaninauts
#
# Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?
import math


# Solution 1
#
# For this problem we can use the combination formula -> C = n! / (n-p)! * p!
# C = routes
# n = the number of moves = grid size * 2
# p = the size of the grid = size
def solve():
    size = 20
    return math.factorial(size*2) / (math.factorial(size) * math.factorial(size))


if __name__ == "__main__":
    print(solve())
