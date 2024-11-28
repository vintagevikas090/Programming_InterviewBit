'''
Problem Description

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:

Input:

1 2 3
4 5 6
7 8 9
Return the following:
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input: 
1 2
3 4
Return the following: 
[
  [1],
  [2, 3],
  [4]
]
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        
        result = [[] for i in range(2*n - 1)]
        # since there are 2n-1 lists for n*n matrix
        
        for i in range(n):
            for j in range(n):
                result[i+j].append(A[i][j])
        return result
        

'''
for the matrix given as
   A00, A01, A02
   A10, A11, A12
   A20, A21, A22

the diagonal antidiagonal element's (i+j) is same
----> Hence they have to be placed in the same list i.e.    (i+j)th
'''
