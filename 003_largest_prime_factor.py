#
# Eduardo Stuani Solutions for Project Euler Problem Number 3
# https://github.com/stuaninauts
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# Solution 1
#
# Not an efficient method but can fit in any case
# def solve():
#     return largest_factor(13195)
#
#
# def primes(num):
#     prime_numbers = []
#     if num <= 1:
#         return prime_numbers
#
#     for a in range(1, num+1):
#         x = 0
#         for b in range(1, a+1):
#             if a % b == 0:
#                 x += 1
#         if x == 2:
#             prime_numbers.append(a)
#     return prime_numbers
#
#
# def largest_factor(num):
#     prime_numbers = primes(num)
#     prime_factors = []
#     for a in prime_numbers:
#         if num % a == 0:
#             prime_factors.append(a)
#             num /= a
#     return max(prime_factors)
#
#


# Solution 2
# Efficient method for this case in specific
# Obs: this solution doesn't work in some cases,
# for example when the number is a perfect square, like 9, 16, 25, etc.
def solve():
    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
        i += 1

    return n


if __name__ == "__main__":
    print(solve())
