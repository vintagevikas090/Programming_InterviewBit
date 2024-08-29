'''
Problem Description
 
 

You are given an array of N integers, A1, A2 ,..., AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.


Problem Constraints
1 <= |A| <= 105
-109 <= Ai <= 109


Input Format
The first argument is an integer array A.


Output Format
Return an integer equal to the maximum value of f(i, j)


Example Input
A = [1, 3, -1]


Example Output
5


Example Explanation
Given A = [1, 3, -1], 
f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
The maximum value is 5, which is of f(2, 3)
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        '''Not optimal'''
        
        # max_sum = -10000000000
        # for i in range(0, len(arr)):
        #     for j in range(i, len(arr)):
        #         c_s = abs(arr[i]-arr[j]) + abs(i-j)
        #         if c_s > max_sum:
        #             max_sum = c_s
        # return max_sum
        
        max1 = max2 = -float('inf')
        min1 = min2 = float('inf')
        
        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            min1 = min(min1, A[i] + i)
            max2 = max(max2, A[i] - i)
            min2 = min(min2, A[i] - i)
            
        return max(max1 - min1, max2 - min2)

'''
when the mode is opened for both -> there will be for case 
two are identical to other two
'''