'''
Reverse a linked list using recursion.

Example :
 Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.

Constraints:

The number of nodes in the list is the range [0, 5000].

-5000 <= Node.val <= 5000


 '''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, head):
        if head is None or head.next is None:
            return head
            
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
