'''
Problem Description
 
 

Given a list of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.


Problem Constraints
1 <= |A| <= 105
0 <= Ai <= 109


Input Format
The first argument is an integer array A.


Output Format
Return a string representing the largest number formed


Example Input
A = [3, 30, 34, 5, 9]


Example Output
9534330


Example Explanation
Largest possible number that can be formed is 9534330
'''



from functools import cmp_to_key
# module is required of using custome camparasion function

class Solution:
    # @param A : tuple of integers
    # @return a strings
    
    def compare(self, x, y):
        if x+y > y+x:
            return -1  # indicating x should come before y(***)
        elif y+x > x+y:
            return 1   # y before x
        else:
            return 0  # order doesn't matter
    
    def largestNumber(self, A):
        arr = [str(i) for i in A]
        
        arr.sort(key= cmp_to_key(self.compare))
        
        result = ''.join(arr)
        
        # if all ele are zero
        if result[0] =='0':
            return '0'
        
        return result


'''
(***)
Why return -1 for x+y>y+x?
The sort() method in Python sorts in ascending order by default.
By returning -1, we tell the sorting algorithm to place x before 𝑦
'''
