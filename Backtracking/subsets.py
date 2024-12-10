'''
Problem Description
 
 

Given a set of distinct integers, A, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.


Problem Constraints
0 <= |A| <= 20


Input Format
The first argument is an integer array A.


Output Format
Return array of all different possible subsets


Example Input
A = [1, 2, 3]


Example Output
[
 [],
 [1],
 [1, 2],
 [1, 2, 3],
 [1, 3],
 [2],
 [2, 3],
 [3],
]

'''

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsets(self, A):
		if len(A) == 0:
			return [[]]
		A.sort()
		
		res = [[]]
		for i in range(len(A)):
			s_o = self.subsets(A[i+1:])
			for j in s_o:
				res.append([A[i]]+j)
				
		return res
