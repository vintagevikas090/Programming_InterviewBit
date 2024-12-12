'''
Problem Description

Given a Binary Tree A containing N nodes.

You need to find the path from Root to a given node B.

NOTE:

No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.


Problem Constraints
 1 <= N <= 105 

 1 <= Data Values of Each Node <= N

 1 <= B <= N



Input Format
First Argument represents pointer to the root of binary tree A.

Second Argument is an integer B denoting the node number.



Output Format
Return an one-dimensional array denoting the path from Root to the node B in order.



Example Input
Input 1:

 A =

           1
         /   \
        2     3
       / \   / \
      4   5 6   7 


B = 5

Input 2:

 A = 
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


B = 1




Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [1]


Example Explanation
Explanation 1:

 We need to find the path from root node to node with data value 5.
 So the path is 1 -> 2 -> 5 so we will return [1, 2, 5]
Explanation 2:

 We need to find the path from root node to node with data value 1.
 As node with data value 1 is the root so there is only one node in the path.
 So we will return [1]


 '''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def node_to_root(self, root, data):
        if root is None:
            return []
            
        if root.val == data:
            return [root.val]
        
        # looking for the path in left part 
        left_output = self.node_to_root(root.left, data)
        if len(left_output) != 0:
            left_output.append(root.val)
            return left_output
    
        # looking for path in right side
        right_output = self.node_to_root(root.right, data)
        if len(right_output) != 0:
            right_output.append(root.val)
            return right_output
        else:
            return [] # ele is not there
    
    def solve(self, A, B):
        node_to_root_path = self.node_to_root(A, B)
        if len(node_to_root_path) != 0:
            return node_to_root_path[::-1] # we need the root to node path
        else:
            return []
