#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 4
# https://github.com/stuaninauts
#
# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


# Solution 1
def solve():
    cp = 0

    for i in range(1, 1000):
        for j in range(1, 1000):
            n = i * j
            ni = int(''.join(reversed(str(n))))
            if n == ni:
                if n > cp:
                    cp = n

    return cp


if __name__ == "__main__":
    print(solve())
