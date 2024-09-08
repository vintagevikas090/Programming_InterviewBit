'''
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def insertionSortList(self, head):
		if head is None or head.next is None:
            return head
        
        sorted_head = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            if sorted_head is None or curr.val < sorted_head.val:
                curr.next = sorted_head
                sorted_head = curr
            else:
                temp = sorted_head
                while temp.next is not None and temp.next.val < curr.val:
                    temp = temp.next
                    
                curr.next = temp.next
                temp.next = curr
                
            curr = next_node
        
        return sorted_head
