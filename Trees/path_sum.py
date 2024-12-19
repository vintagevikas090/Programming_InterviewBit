'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
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
    def checkPathSum(self, root, curr_sum, target_sum):
        if root is None:
            return 0

        curr_sum += root.val
        
        if root.left is None and root.right is None:
            if curr_sum == target_sum:
                return 1
            else:
                return 0

        left_has_path = self.checkPathSum(root.left, curr_sum, target_sum)
        right_has_path = self.checkPathSum(root.right, curr_sum, target_sum)

        if left_has_path or right_has_path:
            return 1
        else:
            return 0
    
    
	def hasPathSum(self, A, B):
        return self.checkPathSum(A, 0, B)
