'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.

Example :

Input : 
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return : 
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
    def build_tree(self, postOrder, inOrder, n):
        if n<=0 :
            return None
        rootData = postOrder[-1]
        rootIndex = inOrder.index(rootData)
        left_data_of_root = inOrder[:rootIndex]
        right_data_of_root = inOrder[rootIndex+1:]
        left_nodes_no = len(left_data_of_root)
        right_nodes_no = n - left_nodes_no -1
        
        root = TreeNode(rootData)
        root.left = self.build_tree(postOrder[:left_nodes_no],left_data_of_root , left_nodes_no)
        root.right = self.build_tree(postOrder[left_nodes_no:left_nodes_no+right_nodes_no] ,right_data_of_root, right_nodes_no)
        return root
    
    
	def buildTree(self, A, B):
        return self.build_tree(A, B, len(A))
