'''
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].

Using recursion is not allowed.
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
	def preorderTraversal(self, root):
		if root is None:
			return []
		if root.left is None and root.right is None:
			return [root.val]
		
		stack = [root]
		result = []
		
		while stack :
			curr = stack.pop()
			result.append(curr.val)
			
			# add left node after right -> becz we need the left to pop out first
			if curr.right is not None:
				stack.append(curr.right)
			if curr.left is not None:
				stack.append(curr.left)
		
		return result
