'''
Given a binary tree, return the inorder traversal of its nodes values.

NOTE: Using recursion is not allowed.



Problem Constraints
 1 <= number of nodes <= 105



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return an integer array denoting the inorder traversal of the given binary tree.



Example Input
Input 1:

   1
    \
     2
    /
   3
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [1, 3, 2]
Output 2:

 [6, 1, 3, 2]


Example Explanation
Explanation 1:

 The Inorder Traversal of the given tree is [1, 3, 2].
Explanation 2:

 The Inorder Traversal of the given tree is [6, 1, 3, 2].

 '''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, root):
		if root is None:
			return []
		if root.left is None and root.right is None:
			return [root.val]
		
		curr = root
		stack = []
		result = []
		
		while curr or stack:
			# LrR -> we need the left most node first, then have to move upwards again
			while curr:
				stack.append(curr)
				curr = curr.left
			
			# this is the left most after loop executes
			curr = stack.pop()
			result.append(curr.val)
			
			curr = curr.right
		
		return result
