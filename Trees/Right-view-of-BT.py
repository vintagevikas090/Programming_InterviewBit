'''
Problem Description

Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.



Problem Constraints
1 <= Number of nodes in binary tree <= 105

0 <= node values <= 109 



Input Format
First and only argument is an pointer to the root of binary tree A.



Output Format
Return an integer array denoting the right view of the binary tree A.



Example Input
Input 1:

        1
      /   \
     2    3
    / \  / \
   4   5 6  7
  /
 8 
Input 2:

    1
   /  \
  2    3
   \
    4
     \
      5


Example Output
Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]

 '''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def right_view(self, root, level, result):
        if root is None:
            return result
        # we add one ele at each level, so len will inc by one each time and so does the level (in rec call)
        if level == len(result):
            result.append(root.val)
        
        self.right_view(root.right, level + 1, result) # firstly right side is called
        self.right_view(root.left, level + 1, result)
        
        return result
    
    def solve(self, A):
        return self.right_view(A, 0, [])
        
