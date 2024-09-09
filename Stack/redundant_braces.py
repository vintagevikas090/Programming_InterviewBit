'''
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.



Problem Constraints
1 <= |A| <= 105



Input Format
The only argument given is string A.



Output Format
Return 1 if A has redundant braces, else return 0.



Example Input
Input 1:

 A = "((a+b))"
Input 2:

 A = "(a+(a+b))"
Input 3:

 A = "((a*b)+(c+d))"


Example Output
Output 1:

 1
Output 2:

 0
Output 3:

 0


Example Explanation
Explanation 1:

 ((a+b)) has redundant braces so answer will be 1.
Explanation 2:

 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.
Explanation 3:

 ((a*b)+(c+d)) doesn't have have any redundant braces so answer will be 0.
 '''

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, string):
        stack = []
    
        for char in string:
            if char == ')':
                count = 0 
                # Check elements inside para until we find (
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    if top in '+-*/':  # Check if there's an operator
                        count += 1
                        
                # pop '('
                stack.pop() 
                
                # If no operator is found between the para -> it's redundant
                if count == 0:
                    return 1
            else:
                stack.append(char)
            
        return 0
