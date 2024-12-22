'''
You are climbing a stair case and it takes A steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Input Format:

The first and the only argument contains an integer A, the number of steps.
Output Format:

Return an integer, representing the number of ways to reach the top.
Constrains:

1 <= A <= 36
Example :

Input 1:

A = 2 Output 1:

2 Explanation 1:

[1, 1], [2] Input 2:

A = 3 Output 2:

3 Explanation 2: 

[1 1 1], [1 2], [2 1]

'''

class Solution:
	# @param A : integer
	# @return an integer
    
    # fun(n) -> no of ways to go from nth step to top 
    def fun(self, n, dp):
        if n == 1:
            return 1
        
        if n == 2: # two ways[(1, 1), (2)]
            return 2
    
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fun(n-1, dp) + self.fun(n-2, dp)
        return dp[n]
    
	def climbStairs(self, A):
        dp = [-1] * (A+1) # 1 based indexing
        return self.fun(A, dp)
        
        
    # size (n+1) -> is for 1 based indexing in dp
    # i.e. dp[1] -> no of ways to climb 1 step
    # dp[2] -> no of ways to climb 2 step
