'''
Given a string S, reverse the string using stack.

Example :

Input : "abc"
Return "cba"
'''

class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        if len(A) <= 1:
            return A 
        
        stack = []
        for char in A:
            stack.append(char)
        
        rev_str = ''
        while len(stack) != 0:
            rev_str += stack.pop()
        return rev_str
