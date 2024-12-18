'''
Problem Description
 
 

Given preorder and inorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.


Problem Constraints
1 <= |A| <= 105
|A| == |B|


Input Format
The first argument is an integer array A representing the preorder traversal.
The second argument is an integer array B representing the inorder traversal.


Output Format
Return the pointer to the root node of the tree.


Example Input
Preorder : [1, 2, 3]
Inorder  : [2, 1, 3]


Example Output
            1
           / \
          2   3
'''


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def Build_tree(self, InO, PreO, n):
        if n<=0 :
            return None
            
        rootData = PreO[0]
        rootIndex = InO.index(rootData)
        
        InO_left = InO[:rootIndex]
        InO_right = InO[rootIndex+1:]
        
        left_nodes_no = len(InO_left)
        right_nodes_no = len(InO_right)
        
        root = TreeNode(rootData)
        root.left = self.Build_tree(InO_left, PreO[1:1+left_nodes_no], left_nodes_no)
        root.right = self.Build_tree(InO_right, PreO[1+left_nodes_no:], right_nodes_no)
        return root
        
    
	def buildTree(self, A, B):
        return self.Build_tree(B, A, len(A))
