'''
Problem Description

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:  

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.


Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109


Input Format
The first and the only argument of input contains an integer array A, of length N.

Output Format
Return an array of integers, that is a subarray of A that satisfies the given conditions.


Example Input
Input 1:

 A = [1, 2, 5, -7, 2, 3]
Input 2:

 A = [10, -1, 2, 3, -4, 100]


Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [100]


Example Explanation
Explanation 1:

 The two sub-arrays are [1, 2, 5] [2, 3].
 The answer is [1, 2, 5] as its sum is larger than [2, 3].
Explanation 2:

 The three sub-arrays are [10], [2, 3], [100].
 The answer is [100] as its sum is larger than the other two.

'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, a):
        max_sum, max_len, max_start = -1, 0, -1
        curr_sum, curr_len, curr_start = 0, 0, 0
        
        for i in range(len(a)):
            if a[i] >= 0:
                curr_sum += a[i]
                curr_len += 1
            else:
                if ((curr_sum > max_sum) or 
                    (curr_sum == max_sum and curr_len > max_len) or 
                    (curr_sum == max_sum and curr_len == max_len and curr_start < max_start)):
                    max_sum = curr_sum
                    max_len = curr_len
                    max_start = curr_start
                
                curr_len = 0
                curr_sum = 0
                curr_start = i + 1  # new subarray start after the -ve number
        
        # checking for the last subarray becz we only update the values 
        # once the -ve number is encounterd (see at the end)
        if ((curr_sum > max_sum) or 
            (curr_sum == max_sum and curr_len > max_len) or
            (curr_sum == max_sum and curr_len == max_len and curr_start < max_start)):
            max_sum = curr_sum
            max_len = curr_len
            max_start = curr_start
            
        if max_start == -1:
            return []
        
        return a[max_start:max_start+max_len]
        
        
        
'''     A = [1, 2, 5, -7, 2, 3]
        During the loop:
        The first sub-array [1, 2, 5] is encountered and compared when -7 is reached.
        The second sub-array [2, 3] is found, but since the array ends after 3, 
        there is no negative number to trigger the comparison of [2, 3] against [1, 2, 5].
        Without the final check, if the array ends with a non-negative sub-array, it could be missed.
'''
