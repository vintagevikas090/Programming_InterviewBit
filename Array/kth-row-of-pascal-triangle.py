'''
Problem Description

Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3


Return : [1,3,3,1]

Note: k is 0 based. k = 0, corresponds to the row [1]. 
'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def gen_pascal(self, k):
        import math
        result = []
        for i in range(k+1):
            row = []
            for j in range(i+1):
                val = (math.factorial(i) // (math.factorial(i-j) * math.factorial(j)))
                row.append(val)
            result.append(row)
        return result
            
    
    
    def getRow(self, k):
        arr = self.gen_pascal(k)
        return arr[k]
