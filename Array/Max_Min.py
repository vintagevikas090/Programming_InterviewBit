'''
Max Min
Programming
Arrays
easy
77.3% Success

363

28

Bookmark
Asked In:
Problem Description

Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

NOTE: You should make minimum number of comparisons.



Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the sum Maximum and Minimum element in the given array.



Example Input
Input 1:

 A = [-2, 1, -4, 5, 3]
Input 2:

 A = [1, 3, 4, 1]


Example Output
Output 1:

 1
Output 2:

 5


Example Explanation
Explanation 1:

 Maximum Element is 5 and Minimum element is -4. (5 + (-4)) = 1. 
Explanation 2:

 Maximum Element is 4 and Minimum element is 1. (4 + 1) = 5.
 '''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # return min(A) + max(A)
      
        maxVal = -10000000000
        minVal = 10000000000
        left, right = 0, len(A)-1
        while left <= right:
            maxVal = max(maxVal, A[left], A[right])
            minVal = min(minVal, A[left], A[right])
            left += 1
            right -= 1
        
        return maxVal + minVal
