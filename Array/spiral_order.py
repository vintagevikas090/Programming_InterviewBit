'''
Problem Description
 
 

Given a matrix of M * N elements (M rows, N columns), return all elements of the matrix in spiral order.


Problem Constraints
1 <= M, N <= 1000


Input Format
The first argument is a matrix A.


Output Format
Return an array of integers representing all elements of the matrix in spiral order.


Example Input
A = 
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]


Example Output
[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''


class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, arr):
        result = []
        if len(arr) == 0:
            return result
        
        top, bottom = 0, len(arr)-1
        left, right = 0, len(arr[0])-1
        
        while top <= bottom and left <= right:
            #1
            for i in range(left, right + 1):
                result.append(arr[top][i])
            top += 1
            
            #2
            for j in range(top, bottom+ 1):
                result.append(arr[j][right])
            right -= 1
            
            #3
            if top <= bottom:
                for i in range(right, left-1 , -1):
                    result.append(arr[bottom][i])
                bottom -= 1
            
            #4 
            if left <= right:
                for j in range(bottom, top -1 , -1):
                    result.append(arr[j][left])
                left += 1
                
        return result
