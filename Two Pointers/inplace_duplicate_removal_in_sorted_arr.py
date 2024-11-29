'''
Given a sorted array A consisting of duplicate elements.

Your task is to remove all the duplicates and return the length of the sorted array of distinct elements consisting of all distinct elements present in A.

Note: You need to update the elements of array A by removing all the duplicates

 



Problem Constraints
1 <= |A| <= 106
1 <= Ai <= 2 * 109


Input Format
First and only argurment containing the integer array A.



Output Format
Return a single integer, as per the problem given.


Example Input
Input 1:

A = [1, 1, 2]
Input 2:

A = [1, 2, 2, 3, 3]


Example Output
Output 1:

2
Output 2:

3


Example Explanation
Explanation 1:

Updated Array: [1, 2, X] after rearranging. Note that there could be any number in place of x since we dont need it.
We return 2 here.
Explanation 2:

Updated Array: [1, 2, 3, X, X] after rearranging duplicates of 2 and 3.
We return 3 from here.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicatesHelper(self, arr):
        idx = 1  # to keep the track for the position of uniques
        # hence it should not inc when duplicate is encountered
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[idx] = arr[i]
                idx += 1
                
        # unique part is only upto idx  
        return arr[:idx]
          
        
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        l = self.removeDuplicatesHelper(A)
        return len(l)
