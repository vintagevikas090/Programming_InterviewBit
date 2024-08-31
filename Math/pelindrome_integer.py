'''
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.



Problem Constraints
INT_MIN <= A <= INT_MAX


Input Format
The first argument is an integer A.


Output Format
Return 1 if A is a Palindrome Integer else return 0.


Example Input
Input 1:
A = 12121
Input 2:
A = 123


Example Output
Output 1:
1
Output 2:
0
'''

class Solution:
    # @param A : integer
    # @return an integer
    
    def digit_at_ith_place(self, num, i):
        return ((num % 10**(i+1))//10**i)
        # assuming 1st digit at 0th place
    
    def no_of_digits(self, num):
        digits = 0
        while num > 0:
            num = num // 10
            digits += 1
        return digits
    
    def isPalindrome(self, n):
        if n < 0:
            return 0
        if n < 10:
            return 1
        
        digit = self.no_of_digits(n)
        left, right = 0, digit-1
        
        while left < right:
            left_digit = self.digit_at_ith_place(n, left)
            right_digit = self.digit_at_ith_place(n, right)
            if left_digit != right_digit:
                return 0
            left += 1
            right -= 1
        return 1
        
        
