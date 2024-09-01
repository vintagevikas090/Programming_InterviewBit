'''
Problem Description
 
 

Given a sorted array of integers A(0 based index) of size N, find the starting and the ending position of a given integer B in array A.

Your algorithm's runtime complexity must be in the order of O(log n).

Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].



Problem Constraints
1 <= N <= 106

1 <= A[i], B <= 109



Input Format
The first argument given is the integer array A.

The second argument given is the integer B.



Output Format
Return an array of size 2, such that the first element = starting position of B in A and the second element = the ending position of B in A if B is not found in A return [-1, -1].



Example Input
Input 1:

 A = [5, 7, 7, 8, 8, 10]
 B = 8
Input 2:

 A = [5, 17, 100, 111]
 B = 3


Example Output
Output 1:

 [3, 4]
Output 2:

 [-1, -1]


Example Explanation
Explanation 1:

 The first occurence of 8 in A is at index 3.
 The second occurence of 8 in A is at index 4.
 ans = [3, 4]
Explanation 2:

 There is no occurence of 3 in the array.
 '''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def first_occurrence(self, arr, val):
        left, right = 0, len(arr)-1
        result = -1
        
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] == val:
                result = mid
                # don't stop. search in the left from mid (if earlier this ele is present)
                right = mid - 1
            
            elif arr[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        
        return result
    
    def last_occurrence(self, arr, val):
        left, right = 0, len(arr)-1
        result = -1
        
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] == val:
                result = mid
                # don't stop. search in the right from mid (if after this, ele is present)
                left = mid + 1
            
            elif arr[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        
    def searchRange(self, A, B):
        a = self.first_occurrence(A, B)
        if a == -1:
            return [-1, -1]
        b = self.last_occurrence(A, B)
        return [a, b]
