'''
Problem Description

Given a number A. Find the fatorial of the number.



Problem Constraints
1 <= A <= 100
'''

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        fact = 1
        for i in range(A, 0, -1):
            fact *= i
        return fact
