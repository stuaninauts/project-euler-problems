#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 10
# https://github.com/stuaninauts
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import math


# Solution 1
def solve():
    num = 2000000
    primes = list()

    for i in range(2, num+1):
        if is_prime(i):
            primes.append(i)

    return sum(primes)


# Return if the number is prime or not
def is_prime(x):
    # I don't do this test because in line 33 I put 2 as the starting point of the sequence
    # if x <= 1:
    #     return False
    if x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


if __name__ == "__main__":
    print(solve())


