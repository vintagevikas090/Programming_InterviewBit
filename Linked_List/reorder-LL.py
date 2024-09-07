'''
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,

Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        
        # find the mid
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # rev the second half
        prev, curr = None, slow
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        ptr1, ptr2 = head, prev
        while ptr2 and ptr2.next:
            ptr1_next, ptr2_next = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = ptr1_next
            ptr1 = ptr1_next
            ptr2 = ptr2_next
    
        return head
        
