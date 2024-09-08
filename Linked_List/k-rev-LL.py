'''
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

NOTE : The length of the list is divisible by K

Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseLL(self, head):
        prev, curr = None, head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev, head
    
    def reverseList(self, head, k):
        if head is None or head.next is None:
            return head
        if k <= 1: 
            return head
        # cut the first k nodes (first part)
        temp = head
        for i in range(1, k):
            if temp.next is not None:
                temp = temp.next
        smallHead = temp.next
        temp.next = None
        
        # rev the first part 
        newHead, tail = self.reverseLL(head)

        newSmallHead = self.reverseList(smallHead, k)
        
        # join with the rec output
        tail.next = newSmallHead
        return newHead
