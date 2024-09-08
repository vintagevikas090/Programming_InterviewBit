'''
Merge two sorted linked lists and return it as a new list. 

The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1 is None and head2 is None:
            return None
        
        merged = ListNode(0)
        merged_tail = merged
        
        ptr1, ptr2 = head1, head2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                merged_tail.next = ptr1
                merged_tail = merged_tail.next
                ptr1 = ptr1.next
            else:
                merged_tail.next = ptr2
                merged_tail = merged_tail.next
                ptr2 = ptr2.next
            
        if ptr1 is not None:
            merged_tail.next = ptr1
        if ptr2 is not None:
            merged_tail.next = ptr2
            
        
        return merged.next            
