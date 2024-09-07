'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Problem approach completely explained :

Complete code in the hints section.


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
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        ptr1, ptr2 = headA, headB
        
        while ptr1 != ptr2:
            if ptr1 is not None:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2 is not None:
                ptr2 = ptr2.next
            else:
                ptr2 = headA
        return ptr1
