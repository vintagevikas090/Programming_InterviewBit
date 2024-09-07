'''
Problem Description

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, head):
        if head is None:
            return head
        
        visited = set()
        temp = head
        while temp is not None:
            if temp in visited:
                return temp
            visited.add(temp)
            temp = temp.next
            
        return None



# sol 2 -> floyd's cycle detection method
class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, head):
        if head is None or head.next is not None:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if it is -> cycle is present
            if slow == fast:
                break
        
        # if cycle is not there, fast ptr will reach the end to become None
        if fast is None or fast.next is None:
            return None
            
        # to find the node where the cycle begins
        # set slow at head, keeping fast where it was
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # the point where slow and fast meet -> node where the cycle begins
        return slow
        
