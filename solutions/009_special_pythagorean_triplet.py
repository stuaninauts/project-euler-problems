#
# Eduardo Stuani Solution(s) for Project Euler Problem Number 9
# https://github.com/stuaninauts
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# Solution 1
def solve():
    num = 1000
    for a in range(1, num+1):
        for b in range(1, num+1):
            c = num - a - b
            if a * a + b * b == c * c:
                return str(a * b * c)


if __name__ == "__main__":
    print(solve())
