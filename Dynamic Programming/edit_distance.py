'''
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:

Return an integer, representing the minimum number of steps required.
Constraints:

1 <= length(A), length(B) <= 450
Examples:

Input 1:
    A = "abad"
    B = "abac"

Output 1:
    1

Explanation 1:
    Operation 1: Replace d with c.

Input 2:
    A = "Anshuman"
    B = "Antihuman"

Output 2:
    2

Explanation 2:
    => Operation 1: Replace s with t.
    => Operation 2: Insert i.

    '''

class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
    
    def fun(self, s1, s2, i, j, dp):
        
        if i == len(s1): # if done with s1 -> add remamining chars from s2
            return len(s2) - j
            
        if j == len(s2):
            return len(s1) - i 
        
        if (i, j) in dp:
            return dp[(i,j)]
        
        # if chars are same -> no operation
        if s1[i] == s2[j]:
            dp[(i,j)] = self.fun(s1, s2, i+1, j+1, dp)
        else:
            # replace, insert or del -> in all case we are doing one operation
            option1 = self.fun(s1, s2, i+1, j+1, dp) + 1
            option2 = self.fun(s1, s2, i, j+1, dp) + 1
            option3 = self.fun(s1, s2, i+1, j, dp) + 1
            
            dp[(i, j)] = min(option1, option2, option3)
        
        return dp[(i,j)]
        
    
    
	def minDistance(self, A, B):
        dp = {}
        
        return self.fun(A, B, 0, 0, dp)
