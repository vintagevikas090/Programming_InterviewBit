'''
Given a string A, containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
Note:  The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


Problem Constraints
1 <= |A| <= 106


Input Format
The first and only argument is a string A.


Output Format
Return an integer, 0 / 1 ( 0 for false, 1 for true )


Example Input
Input 1:
A = "()[]{}"
Input 2:
A = "([)]"


Example Output
Output 1:
1
Output 1:
0
'''
class Solution:
    # @param A : string
    # @return an integer
    def isopening(self, char):
        if char == '(' or char == '[' or char == '{':
            return True
        else:
            return False
    
    def isValid(self, string):
        stack = []
        correct_match = {')':'(', ']':'[', '}':'{'}
        for char in string:
            if self.isopening(char):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return 0
                else:
                    top = correct_match[char]
                    if stack[-1] != top:
                        return 0
                    stack.pop()
        
        if len(stack) != 0:
            return 0
        else:
            return 1
