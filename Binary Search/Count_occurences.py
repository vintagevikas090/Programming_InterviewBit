'''
Given a sorted array of integers, find the number of occurrences of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return 0

**Example : **

Given [5, 7, 7, 8, 8, 10] and target value 8,

return 2.

'''

# sol 1 
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    
    # this return the first occurence index of the val
    def binary_search(self, arr, val):
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
    
    def findCount(self, A, B):
        idx = self.binary_search(A, B)
        if idx == -1:
            return 0
            
        count = 1
        while idx + 1 < len(A) and A[idx+ 1] == A[idx]:
            count += 1
            idx += 1
            
        return count



# sol 2 
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    
    # this return the first occurence index of the val
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
    
    def findCount(self, A, B):
        first = self.first_occurrence(A, B)
        if first == -1:
            return 0
            
        last = self.last_occurrence(A, B)
        return last - first + 1
        

