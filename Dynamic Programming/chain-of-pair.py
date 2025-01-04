'''
Given a N * 2 array A where (A[i][0], A[i][1]) represents the ith pair.

In every pair, the first number is always smaller than the second number.

A pair (c, d) can follow another pair (a, b) if b < c , similarly in this way a chain of pairs can be formed.

Find the length of the longest chain subsequence which can be formed from a given set of pairs.


Note: A subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.



Problem Constraints
1 <= N <= 103

1 <= A[i][0] < A[i][1] <= 104



Input Format
First and only argument is an 2D integer array A of size N * 2 representing the N pairs.



Output Format
Return a single integer denoting the length of longest chain subsequence of pairs possible under given constraint.



Example Input
Input 1:

 A = [  [5, 24]
        [39, 60]
        [15, 28]
        [27, 40]
        [50, 90]
     ]
Input 2:

 
A = [   [10, 20]
        [1, 2]
     ]


Example Output
Output 1:

 3
Output 2:

 1


Example Explanation
Explanation 1:

 Longest chain that can be formed is of length 3, and the chain is [ [5, 24], [27, 40], [50, 90] ]
Explanation 2:

 Longest chain that can be formed is of length 1, and the chain is [ [1, 2] ] or [ [10, 20] ]
 '''




class Solution:
    def solve(self, A):
        n = len(A)
        dp = [1] * n  
        for i in range(n):
            # check all pair before idx i 
            for j in range(i):
                if A[i][0] > A[j][1]:  
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)  


# dp[i] represents the longest chain that ends with the pair A[i]

# dp[i] is updated to be the maximum of:
# The current value of dp[i] (which represents the longest chain ending at A[i] without including A[j]).
# dp[j] + 1 (which represents the longest chain ending at A[j], plus the new pair A[i] that can follow A[j])
