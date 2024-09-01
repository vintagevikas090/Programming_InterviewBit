'''
Problem Description
Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:
A bitonic sequence is a sequence of numbers that first increases monotonically and then decreases monotonically. In simpler terms, a bitonic sequence consists of two parts:
Increasing Sequence: The first part of the sequence has elements that are strictly increasing.
Decreasing Sequence: The second part of the sequence has elements that are strictly decreasing.

Problem Constraints
3 <= N <= 105

1 <= A[i], B <= 108

Given array always contain a bitonic point.

Array A always contain distinct elements.



Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.



Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.



Example Input
Input 1:

 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:

 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30


Example Output
Output 1:

 3
Output 2:

 -1


Example Explanation
Explanation 1:

 B = 20 present in A at index 3
Explanation 2:

 B = 30 is not present in A
 '''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bin_search_asc_arr(self, arr, val, left, right):
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
    def bin_search_dsc_arr(self, arr, val, left, right):
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        
    def find_max_in_bitonic(self, arr):
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        return left    # or right
    
    def solve(self, A, B):
        # finding max val index
        peak = self.find_max_in_bitonic(A)
        
        # 0 to peak -> inc arr 
        index = self.bin_search_asc_arr(A, B, 0, peak)
        
        if index != -1:
            return index
        
        # if index == -1 -> ele not in inc arr -> find in dec part
        return self.bin_search_dsc_arr(A, B, peak+1, len(A)-1)
