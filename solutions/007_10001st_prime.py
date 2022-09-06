#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 7
# https://github.com/stuaninauts
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
import math


# Solution 1
def solve():
    return n_prime(10001)


# Return if the number is prime or not
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


# Count the prime numbers until get the nth prime
def n_prime(n):
    count = 0
    i = 0
    while count != n:
        i += 1
        if is_prime(i):
            count += 1
    return i


if __name__ == "__main__":
    print(solve())
