'''
Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only  argument is the root of the tree A.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input
Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 

'''


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	
	# returns height and is_balance or not
	def isBalancedHelper(self, root):
		if root is None:
			return 0, 0
		if root.left is None and root.right is None:
			return 1, 1
		
		left_h, left_bal = self.isBalancedHelper(root.left)
		right_h, right_bal = self.isBalancedHelper(root.right)
		
		height = max(left_h, right_h) + 1
		
		if abs(left_h - right_h) > 1:
			return height, 0
			
		if left_bal and right_bal:
			return height, 1
		else:
			return height, 0
	
	
    def isBalanced(self, A):
		h, ans = self.isBalancedHelper(A)
		return ans
