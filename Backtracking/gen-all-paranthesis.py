'''
Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.



Problem Constraints
1 <= A <= 10



Input Format
First and only argument is integer A.



Output Format
Return a sorted list of all possible parenthesis.



Example Input
Input 1:

A = 3
Input 2:

A = 1


Example Output
Output 1:

[ "((()))", "(()())", "(())()", "()(())", "()()()" ]
Output 2:

[ "()" ]


Example Explanation
Explanation 1:

 All paranthesis are given in the output list.
Explanation 2:

 All paranthesis are given in the output list.
 '''

class Solution:
    # @param A : integer
    # @return list of strings
    
    def gen_para(self, A, curr, open_count, close_count):
        if len(curr) == 2 * A:
            return [curr]

        res = []

        if open_count < A:
            res += self.gen_para(A, curr + '(', open_count + 1, close_count)
        if close_count < open_count:
            res += self.gen_para(A, curr + ')', open_count, close_count + 1)

        return res
        
    
    def generateParenthesis(self, A):
        return self.gen_para(A, "", 0, 0)



# for valid combination -> open_para == close_para
# so for comb of len 2*A -> open_para_max = A
#                     and for valid para -> close_para_max = open_para_cnt
