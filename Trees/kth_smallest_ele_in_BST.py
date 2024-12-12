'''
Given a binary search tree, write a function to find the kth smallest element in the tree.
NOTE: You may assume 1 <= k <= Total number of nodes in BST


Input Format
The first argument is the root node of the binary tree.
The second argument B is an integer equal to the value of k.


Output Format
Return the value of the kth smallest node.


Example Input
  2
 / \
1   3


and k = 2



Example Output
2


Example Explanation
As 2 is the second smallest element in the tree.

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
    def inorder(self, root):
        result = []
        if root is None:
            return result
        if root.left is None and root.right is None:
            result.append(root.val)
            return result
        
        result += self.inorder(root.left)
        result.append(root.val)
        result += self.inorder(root.right)
    
        return result
            
    
    
	def kthsmallest(self, A, B):
        arr = self.inorder(A)
        return arr[B-1]
