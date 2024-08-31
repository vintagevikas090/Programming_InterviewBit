'''
Given 2 non-negative integers A and B, find gcd(A, B).
GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both A and B fit in a 32-bit signed integer.
NOTE: DO NOT USE LIBRARY FUNCTIONS
'''

# sol1 -> not efficient
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A
        if A == 0:
            return B
        temp = min(A, B)
        for i in range(temp, 0, -1):  # Start from temp and go down to 1
            if A % i == 0 and B % i == 0:
                return i 
        return 1 

# sol2 
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while A != B:
            if A > B:
                A = A - B
            else:
                B = B - A
        return A

# sol3
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while B != 0:
            A, B = B, A % B
        return A
