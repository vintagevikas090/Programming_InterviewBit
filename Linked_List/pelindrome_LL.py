'''
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, head):
        if head is None or head.next is None:
            return 1
        
        # find the mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec_head = slow.next
        # rev the second half
        prev, curr = None, sec_head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        ptr1, ptr2 = head, prev
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return 0
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return 1
