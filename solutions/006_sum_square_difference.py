#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 6
# https://github.com/stuaninauts
#
# The sum of the squares of the first ten natural numbers is,
# 1² + 2² + ... + 10² = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)² = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.


# Solution 1
def solve():
    n = 100
    return square_sum(n) - sum_squares(n)


# Create a list containing all first n natural numbers
# Use the map function for iterate over the list
# Return the sum off all elements from the resulting list
def sum_squares(n):
    return sum(list(map(lambda x: x ** 2, range(1, n+1))))


# Sum all elements from the list containing all first n natural numbers
# Return the square of this sum
def square_sum(n):
    return sum(list(range(1, n+1))) ** 2


if __name__ == "__main__":
    print(solve())
