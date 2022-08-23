#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 1
# https://github.com/stuaninauts
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


# Solution 1
def solve():
    max_value = 1000    # teste
    total = 0

    for i in range(3, max_value):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    print(solve())
