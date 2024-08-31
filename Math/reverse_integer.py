'''
Problem Description

You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer


Look at the example for clarification.



Problem Constraints
N belongs to the Integer limits.



Input Format
Input an Integer.



Output Format
Return a single integer denoting the reverse of the given integer.



Example Input
Input 1:

 x = 123


Input 2:

 x = -123


Example Output
Output 1:

 321


Ouput 2:

 -321
 '''

class Solution:
    # @param A : integer
    # @return an integer
    
    def reverse(self, num):
        temp = abs(num)
        rev_num = 0
        while temp > 0:
            last_digit = temp % 10
            rev_num = rev_num * 10 + last_digit
            temp = temp // 10
        
        if rev_num < -2**31 or rev_num > 2**31 - 1:
            return 0
        
        if num < 0:
            return -rev_num
        
        return rev_num
