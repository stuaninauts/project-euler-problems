#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 5
# https://github.com/stuaninauts
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math


# Solution 1
#
# Simple solution using lcm function included in math lib
# Obs: lcm function only work in Python 3.9 or more recent version
def solve():
    return math.lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


if __name__ == "__main__":
    print(solve())
