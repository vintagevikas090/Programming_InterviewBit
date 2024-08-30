'''
Given a non negative integer A,

find all pair of integers (a, b) such that

a and b are positive integers
a <= b, and
a2 + b2 = A.
0 <= A <= 100000
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def squareSum(self, A):
        ans = []
        a = 1
        
        while a * a <= A:
            b_square = A - a * a
            b = int(b_square**0.5)
            # Check if b*b equals the remainder and a <= b to avoid duplicates
            if b * b == b_square and a <= b:
                ans.append([a, b])
            a += 1
        
        return ans
