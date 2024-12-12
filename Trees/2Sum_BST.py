'''
Given a binary search tree A, where each node contains a positive integer, and an integer B, you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise.



Problem Constraints
1 <= size of tree <= 100000

1 <= B <= 109



Input Format
First argument is the head of the tree A.

Second argument is the integer B.



Output Format
Return 1 if such a pair can be found, 0 otherwise.



Example Input
Input 1:

         10
         / \
        9   20


B = 19

Input 2:

 
          10
         / \
        9   20


B = 40



Example Output
Output 1:

 1
Output 2:

 0
 '''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	
	# get all values in tree
	def get_arr(self, root):
		res = []
		if root is None:
			return res
		if root.left is None and root.right is None:
			res.append(root.val)
			return res
		
		res.append(root.val)
		res += self.get_arr(root.left)
		res += self.get_arr(root.right)
		return res
		
	def pair_sum(self, arr, k):
		n = len(arr)
		if n < 2:
			return 0
		
		seen = set()
		for val in arr:
			expect = k - val
			if expect in seen:
				return 1
			seen.add(val)
		return 0
	
	def t2Sum(self, A, B):
		a = self.get_arr(A)
		return self.pair_sum(a, B)



# better approach -> using inorder 

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	
	def inorder(self, root, k):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 0
		
		curr = root
		stack = []
		seen = set()
		
		while curr or stack:
			# LrR -> we need the left most node first, then have to move upwards again
			while curr:
				stack.append(curr)
				curr = curr.left
			
			# this is the left most after loop executes
			curr = stack.pop()

      # check for complement (#######)
			c = k - curr.val
			if c in seen:
				return 1
      
			seen.add(curr.val)
			
			curr = curr.right
		
		return 0
	
	def t2Sum(self, A, B):
		return self.inorder(A, B)
