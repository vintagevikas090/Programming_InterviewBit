'''
For Given Number A, find if it's a COLORFUL number or not.

COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Return 1 if A is a COLORFUL number, else return 0



Problem Constraints
0 <= A <= 109


Input Format
The first argument is an integer A.


Output Format
Return 1 if A is a COLORFUL number, else return 0


Example Input
A = 23


Example Output
1


Example Explanation
A = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since the product of every digit of a sub-sequence is different.

Output: 1

'''

class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
		A_str = str(A)
		n = len(A_str)
		
		seen_products = set()
		
		for i in range(n):
			product = 1
			for j in range(i, n):        # these two lines
				product *= int(A_str[j])   # gen all possible product 
				
				if product in seen_products:
					return 0
				
				seen_products.add(product)
			
		return 1
