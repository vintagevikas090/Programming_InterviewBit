'''
Problem Description

Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= 109



Input Format
First argument is array A.

Second argument is integer B.



Output Format
Return an integer, the answer to the problem.



Example Input
Input 1:

 A = [1, 3, 5, 6]
B = 5
Input 2:

 A = [1, 3, 5, 6]
B = 2


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 5 is found at index 2.
Explanation 2:

 2 will be inserted ar index 1.

'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        left, right = 0, len(A) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
