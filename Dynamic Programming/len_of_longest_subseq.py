'''
Given a 1D integer array A of length N, find the length of the longest subsequence which is first increasing (strictly) and then decreasing (strictly).



Problem Constraints
0 <= N <= 3000

 -107 <= A[i] <= 107



Input Format
The first and the only argument contains an integer array A



Output Format
Return an integer representing the answer as described in the problem statement.



Example Input
Input 1:

 A = [1, 2, 1]
Input 2:

 A = [1, 11, 2, 10, 4, 5, 2, 1]


Example Output
Output 1:

 3
Output 2:

 6


Example Explanation
Explanation 1:

 [1, 2, 1] is the longest subsequence.
Explanation 2:

 [1 2 10 4 2 1] is the longest subsequence.
'''


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestSubsequenceLength_helper(self, A):
		n = len(A)
		if n == 0:
			return 0
		
		# array for storing len of Longest inc subseq ending at index i 
		inc = [1] * n
		# array for storing len of longest dec subseq starting from indx i 
		dec = [1] * n

		for i in range(1, n):
			for j in range(i):
				# if the A[i] > A[j] -> A[i] can extend the LIS ending at index j -> can possibly form a subseq
				# with the prev seq A[0:j] 
				if A[j] < A[i]:
					# check for the max of the curr LIS len or the len of { (A[0:j] + A[i]) }
					inc[i] = max(inc[i], inc[j] + 1)

		for i in range(n-2, -1, -1):
			for j in range(i+1, n):
				if A[j] < A[i]:
					dec[i] = max(dec[i], dec[j] + 1)

		max_length = 0
		for i in range(n):
			# -1 is there -> becz each ele is considered 2 times (one in inc and one in dec)
			max_length = max(max_length, inc[i] + dec[i] - 1)

		return max_length


	def longestSubsequenceLength(self, A):
		return self.longestSubsequenceLength_helper(A)
