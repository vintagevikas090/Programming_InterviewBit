'''
Find the contiguous subarray within an array, A of length N which has the largest sum.


Problem Constraints
1 <= N <= 106
-1000 <= A[i] <= 1000


Input Format
The first and the only argument contains an integer array, A.


Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.


Example Input
Input 1:
A = [1, 2, 3, 4, -10]
Input 2:
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
'''

'''
To solve the problem of finding the maximum sum of a contiguous subarray, 
0we can use Kadane's Algorithm, which is both efficient and straightforward for this type of problem.

Key Points of Kadane's Algorithm:
Local Maximum: Keep track of the maximum sum of the subarray that ends at the current position.
Global Maximum: Keep track of the overall maximum sum found so far
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, arr):
        max_sum = arr[0]
        curr_sum = arr[0]
        for i in range(1, len(arr)):
            # compare individual element with the sum of the subarray (formed upto now)
            curr_sum = max(arr[i], curr_sum + arr[i])
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum

