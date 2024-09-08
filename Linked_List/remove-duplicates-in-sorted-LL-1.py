'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,

Given 1->1->2, return 1->2.

Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# iterative solution
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    import sys
    sys.setrecursionlimit(10**9)
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
            
        prev = head
        curr = head.next 
        while curr :
            nn = curr.next
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = nn 
        return head 


# recursive sol
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    import sys
    sys.setrecursionlimit(10**9)
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
            
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            return self.deleteDuplicates(head.next)
