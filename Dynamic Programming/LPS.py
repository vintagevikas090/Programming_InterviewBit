'''
Problem Description
 
 

Given a string A, find the common palindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself.

You need to return the length of longest palindromic subsequence in A.

NOTE:

Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.


Problem Constraints
 1 <= |A| <= 1005



Input Format
First and only argument is an string A.



Output Format
Return a integer denoting the length of longest palindromic subsequence in A.



Example Input
Input 1:

 A = "bebeeed"


Example Output
Output 1:

 4


Example Explanation
Explanation 1:

 The longest common pallindromic subsequence is "eeee", which has a length of 4
 '''

class Solution:
    # @param A : string
    # @return an integer
    
    # f(i, j) -> gives the len of LPS for string[i:j]
    def f(self, string, i, j, dp):
        if i == j:
            return 1
        if i > j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        # if this holds -> ith and jth both char contributes to the pelindrome seq
        if string[i] == string[j]:
            dp[i][j] = 2 + self.f(string, i+1, j-1, dp)
        else:
            # neglecting first char
            possiblity1 = self.f(string, i+1, j, dp)
            # neglecting last char
            possiblity2 = self.f(string, i, j-1, dp)
            
            dp[i][j] = max(possiblity1, possiblity2)
        
        return dp[i][j]    
    
    def solve(self, A):
        n = len(A)
        if n <= 1:
            return n
        
        dp = [[-1 for i in range(n)] for j in range(n)]
    
        return self.f(A, 0, n-1, dp)
