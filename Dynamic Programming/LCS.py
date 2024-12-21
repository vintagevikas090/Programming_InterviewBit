'''
Problem Description

Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.



Problem Constraints
1 <= |A|, |B| <= 1005



Input Format
First argument is an string A.

Second argument is an string B.



Output Format
Return the length of such longest common subsequence between string A and string B.



Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"


Example Output
Output 1:

 5


Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5

 '''




import sys
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    
    # f(i, j) -> LCS between str1[i:] and str2[j:]
    
    def lcs(self, dp, str1, str2, i, j):
        if i == len(str1) or j == len(str2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        # char matches -> include in the lcs
        if str1[i] == str2[j]:
            dp[i][j] = 1 + self.lcs(dp, str1, str2, i+1, j+1)
        # otherwise consider only the max out of the two possibilities
        else:
            dp[i][j] = max(self.lcs(dp, str1, str2, i, j+1), self.lcs(dp, str1, str2, i+1, j))  
        
        return dp[i][j]      
    
    def solve(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return 0
        
        dp = [[-1 for i in range(len(B))] for j in range(len(A))]
        
        return self.lcs(dp, A, B, 0, 0)
