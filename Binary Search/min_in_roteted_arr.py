'''
Problem Description
 
 

Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 1 2 4 5 6 7 might become 4 5 6 7 1 2).

Find the minimum element.

The array will not contain duplicates.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        left, right = 0, len(A)-1
        
        while left < right:
            mid = (left+right)//2
            
            # (***) see at the end
            if A[mid] > A[right]:
                left = mid + 1
            else:
                right = mid
        # left == right at the end
        return A[left]
        


'''
Unrotated Array: If the array is not rotated, the first element will be less than or equal to the last element.
In this case, the minimum element is the first element.

(***)
Rotated Array: The minimum element is the only element that is smaller than its previous element. 
In the modified binary search, we search for this inflection point where the rotation happens.
'''
