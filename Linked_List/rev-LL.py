'''
Reverse a linked list. Do it in-place and in one-pass.

For example:

Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
            
        newhead = self.reverseList(head.next)
        tail = head.next
        head.next = None
        tail.next = head
        
        return newhead
