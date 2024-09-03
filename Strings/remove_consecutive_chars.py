'''
Problem Description
 
 

Given a string A and integer B, remove all consecutive same characters that have length exactly B.


NOTE : All the consecutive same characters that have length exactly B will be removed simultaneously.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= |A|



Input Format
First Argument is string A.

Second argument is integer B.



Output Format
Return a string after doing the removals.



Example Input
Input 1:

A = "aabcd"
B = 2
Input 2:

A = "aabbccd"
B = 2


Example Output
Output 1:

 "bcd"
Output 2:

 "d"


Example Explanation
Explanation 1:

 "aa" had length 2.
Explanation 2:

 "aa", "bb" and "cc" had length of 2.
'''


# sol 1 
class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, string, B):
        if B == 1:
          return ''
        stack = []
        
        for char in string:
            if len(stack) == 0:
                stack.append([char, 1])
            else:
                top_char = stack[-1][0]
                if top_char == char:
                    stack[-1][1] += 1
                    
                    if stack[-1][1] == B:
                        stack.pop()
                else:
                    stack.append([char, 1])
        
        res = []
        for char, freq in stack:
            res.append(char * freq)
            # (***)
        
        output = ''.join(res)
        return output
        
        
'''
# we have to consider the freq as well 
# becz if freq of a char is not a multiple of becz
# then the all remaining chars should be considered

say for aaabbbccdddd , B = 4 -> 3 a's and 3 b's and 2 c's should be there in output
'''


# sol2 -> better one (worked for B == 1) 
def solve(self, A, B):
        c = 1
        l = []
        
        for idx, ele in enumerate(A):
            if idx + 1 < len(A):
                if ele == A[idx + 1]:
                    c += 1
                else:
                    if c != B:
                        l.append(ele * c)
                    c = 1

        if c != B:
            l.append(A[-1] * c)

        return ''.join(l)
