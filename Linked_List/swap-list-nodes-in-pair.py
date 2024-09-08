'''
Given a linked list A, swap every two adjacent nodes and return its head.

NOTE: Your algorithm should use only constant space. You may not modify the values in the list; only nodes themselves can be changed.

Problem Constraints
 1 <= |A| <= 106 

Input Format
 The first and the only argument of input contains a pointer to the head of the given linked list. 
Output Format
 Return a pointer to the head of the modified linked list. 

Example Input
 Input 1: 

 A = 1 -> 2 -> 3 -> 4
 Input 2: 

 A = 7 -> 2 -> 1


Example Output
 Output 1: 

 2 -> 1 -> 4 -> 3
 Output 2: 

 2 -> 7 -> 1


Example Explanation
Explanation 1:

 In the first example (1, 2) and (3, 4) are the adjacent nodes. Swapping them will result in 2 -> 1 -> 4 -> 3
Explanation 2:

 In the second example, 3rd element i.e. 1 does not have an adjacent node, so it won't be swapped. 
 '''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    import sys
    sys.setrecursionlimit(10**9)
    
    
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
            
        # cut first two nodes
        temp = head.next
        next_node = temp.next
        temp.next = None

        # rev the first two nodes 
        head.next = None
        temp.next = head
        head = temp

        smallerOutput = self.swapPairs(next_node)
        head.next.next = smallerOutput
        return head
