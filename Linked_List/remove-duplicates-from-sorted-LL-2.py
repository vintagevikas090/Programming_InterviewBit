'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,

Given 1->2->3->3->4->4->5, return 1->2->5.

Given 1->1->1->2->3, return 2->3.
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
    
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head  

        while curr:
            # if curr node is a duplicate 
            if curr.next and curr.val == curr.next.val:
                # go the last occurrence of the 'curr'
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # del all nodes in between
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next
        
        return dummy.next


# recursive solution
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
            # skipping all the duplicates 
            while head.next and head.val == head.next.val :
                head = head.next
            return self.deleteDuplicates(head.next)
