'''
Problem Description
 
 

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.



Problem Constraints
1 <= |A| <= 106
-109 <= Ai <= 109


Input Format
First and only argument is an integer array A.



Output Format
Return 1 if any such integer p is found else return -1.



Example Input
Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


Example Output
Output 1:

 1
Output 2:

 -1


Example Explanation
Explanation 1:

 For integer 2, there are 2 greater elements in the array. So, return 1.
Explanation 2:

 There is no such integer exists.

'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        for i in range(n):
            right_len = n - 1 - i
            if A[i] == right_len:
                # if it is last element
                # since for last element, there should be 0 greter value
                if i == n - 1:
                    return 1
                # considering duplicates
                # if next ele is not same as curr ele, then only return 1 else go to next ele
                if i + 1 < n and A[i] != A[i+1]:
                    return 1
        return -1
