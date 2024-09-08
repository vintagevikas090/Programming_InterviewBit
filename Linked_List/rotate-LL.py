'''
Given a list, rotate the list to the right by k places, where k is non-negative.


Problem Constraints
1 <= B <= 109


Input Format
The first argument is ListNode A, pointing to the head of the list.
The second argument is an integer B, representing the value of k.


Output Format
Return the rotated list.


Example Input
A = 1->2->3->4->5->NULL
B = 2


Example Output
4->5->1->2->3->NULL


Example Explanation
Given list: A = 1->2->3->4->5->NULL
Given B = 2;
After rotating A once, A = 5->1->2->3->4->NULL
After rotating A again, A = 4->5->1->2->3->NULL
Hence after rotating the given list A, for B = 2, return 4->5->1->2->3->NULL
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
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        
        length = 1
        tail = head # will be needed for connection with org head
        while tail.next is not None:
            tail = tail.next
            length += 1
        
        k = k % length
        # connect the last to org head
        tail.next = head
        
        # get to just before the 'newhead' node 
        n = length - k
        temp = head
        for i in range(1, n):
            temp = temp.next
        
        newhead = temp.next
        temp.next = None
        
        return newhead
            
