'''
Problem Description
 
 

Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.


Problem Constraints
3 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A containing N integers.



Output Format
Return 1 if there exist a element that is strictly greater than all the elements on left of it and strictly  smaller than all the elements on right of it else return 0.



Example Input
Input 1:

 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:

 A = [5, 1, 4, 4]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 A[4] = 6 is the element we are looking for.
 All elements on left of A[4] are smaller than it and all elements on right are greater.
Explanation 2:

 No such element exits.

 '''




# logic -> the ele we need the one which satisfies this condition
#       max(left_part) < A[i] < min(right_part)


# not optimal due to O(n2) space
class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        for i in range(1, len(A)-1):
            left = A[:i]
            right = A[i+1:]
            if A[i] > left_max and A[i] < min(right):
                return 1
        return 0


# mroe optimal -> O(n) space

class Solution:
    
    # left_max[i] stores the maximum value among elements from A[0] to A[i-1].
    # right_min[i] stores the minimum value among elements from A[i+1] to A[N-1].
    def perfectPeak(self, A):
        N = len(A)
        if N < 3:
            return 0
        
        left_max = [float('-inf')] * N
        right_min = [float('inf')] * N
        
        for i in range(1, N):
            left_max[i] = max(left_max[i-1], A[i-1])
        
        for i in range(N-2, -1, -1):
            right_min[i] = min(right_min[i+1], A[i+1])
        

        for i in range(1, N-1):
            if left_max[i] < A[i] < right_min[i]:
                return 1
        
        return 0
