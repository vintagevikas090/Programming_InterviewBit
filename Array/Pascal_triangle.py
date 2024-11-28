'''
Problem Description
 
 

Given an integer A, equal to numRows, generate the first numRows of Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from the previous row R - 1.



Problem Constraints
0 <= A <= 25


Input Format
The first argument is an integer A, equal to the numRows.


Output Format
Return an array of array of integers, equal to pascal triangle.


Example Input
A = 5


Example Output
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

'''



      1
     1 1
    1 2 1
   1 3 3 1
#### Pascal triangle using nCr 
        0C0
    1C0   1C1
    2C0   2C1   2C2
3C0   3C1   3C2    3C3


class Solution:
    # @param A : integer
    # @return a list of list of integers
    
    def solve(self, A):
        from math import factorial
        result = []
        for i in range(A):
            row = []
            for j in range(i+1):
                val = (factorial(i)//(factorial(i-j)*factorial(j)))
                row.append(val)
            result.append(row)
        return result
