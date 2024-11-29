'''
Given an array 'A' of sorted integers and another non-negative integer B, find if there exist 2 indices i and j such that A[i] - A[j] = k, i != j.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Try doing this in less than linear space complexity.


Problem Constraints
1 <= |A| <= 106
0 <= B <= 109


Input Format
The first argument is an integer array A.
The second argument is an integer B.


Output Format
Return an integer, 0 / 1 ( 0 for false, 1 for true ) for this problem


Example Input
 A : [1 3 5] 
 B : 4


Example Output
1


Example Explanation
For the given, 
 A : [1 3 5] 
 B : 4
Output : YES
as 5 - 1 = 4
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		if len(A) < 2:
			return 0
			
		i, j, n = 0, 1, len(A)
		
		while j < n:
			if i != j and A[j] - A[i] == B:
				return 1
			elif A[j] - A[i] < B:
				j += 1   # if diff is less, we should increase it(hence move j)
			else: 
				i += 1   # diff is more, so need ot be reduced
				if i == j:  # if i exceeds j
					j += 1
		return 0
