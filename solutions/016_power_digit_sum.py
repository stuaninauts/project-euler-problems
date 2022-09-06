#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 16
# https://github.com/stuaninauts
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


# Solution 1
def solve():
    n = 2
    e = 1000
    x = n**e
    return sum(int(d) for d in str(x))


if __name__ == "__main__":
    print(solve())
