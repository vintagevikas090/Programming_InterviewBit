'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers % 1003.


Problem Constraints
0 <= Node.val <= 9


Input Format
The first argument is TreeNode A, pointing to the root of the tree.


Output Format
Return an integer equal to the total sum of all root-to-leaf numbers % 1003.


Example Input
    1
   / \
  2   3


Example Output
25


Example Explanation
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.

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
    def root_to_leaf(self, root, curr_path):
        if root is None:
            return []
        
        curr_path += str(root.val)
        
        if root.left is None and root.right is None:
            return [curr_path]
        
        left_paths = self.root_to_leaf(root.left, curr_path)
        right_paths = self.root_to_leaf(root.right, curr_path)
        
        return left_paths + right_paths
    
	def sumNumbers(self, A):
        if A is None:
            return 0
        
        possible_nums_str = self.root_to_leaf(A, '')
        
        sum_val = 0
        for str_num in possible_nums_str:
            sum_val += int(str_num)
        
        return sum_val % 1003
      
