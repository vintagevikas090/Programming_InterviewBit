'''
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both arrays ).

The overall run time complexity should be O(log (m+n)).

NOTE: If the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 


Problem Constraints
0 <= |A| <= 106
0 <= |B| <= 106
1 <= |A| + |B| <= 2 * 106


Input Format
The first argument is an integer array A.
The second argument is an integer array B.


Output Format
Return a double value equal to the median.


Example Input
A : [1 4 5]
B : [2 3]


Example Output
3


Example Explanation
Merged A and B will be : [1, 2, 3, 4, 5]
Its median will be 3
'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        # Ensure A is the smaller array (if not -> swap)
        if len(A) > len(B):
            A, B = B, A
        
        m, n = len(A), len(B)
        left, right, half_len = 0, m, (m + n + 1) // 2

        while left <= right:
            # partition index of A
            pi1 = (left + right) // 2
            pi2 = half_len - pi1
            
            # (***)
            if pi1 < m and A[pi1] < B[pi2 - 1]:
                left = pi1 + 1
            elif pi1 > 0 and A[pi1 - 1] > B[pi2]:
                right = pi1 - 1
            else:
                return self.findMedian(pi1, pi2, A, B)

    def findMedian(self, i, j, A, B):
        if i == 0:
            max_of_left = B[j - 1]
        elif j == 0:
            max_of_left = A[i - 1]
        else:
            max_of_left = max(A[i - 1], B[j - 1])

        if (len(A) + len(B)) % 2 == 1:
            return max_of_left

        if i == len(A):
            min_of_right = B[j]
        elif j == len(B):
            min_of_right = A[i]
        else:
            min_of_right = min(A[i], B[j])

        return (max_of_left + min_of_right) / 2.0


'''
***
Binary Search Loop: Adjust the partition indices pi1 for A and pi2 for B:
If the element in the right partition of B is greater than the element in the left partition of A, increase pi1.
If the element in the left partition of A is greater than the element in the right partition of B, decrease pi1.
When the correct partition is found, call computeMedian to calculate the median


Median Calculation:
If the total number of elements is odd, return max_of_left (partition).
If even, return the average of max_of_left and min_of_right (partition).
'''


