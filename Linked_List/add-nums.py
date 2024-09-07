'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list

So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
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
    def addTwoNumbers(self, head1, head2):
        rev_head, rev_tail = None, None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        ptr1, ptr2, carry = head1, head2, 0
        while ptr1 or ptr2 or carry!=0:
            num1, num2 = 0, 0
            if ptr1 is not None:
                num1 = ptr1.val
            if ptr2 is not None:
                num2 = ptr2.val
            
            value = num1 + num2 + carry
            digit = value % 10
            carry = value // 10
            
            new_node = ListNode(digit)
            if rev_head is None:
                rev_head = rev_tail = new_node
            else:
                rev_tail.next = new_node
                rev_tail = rev_tail.next
            
            if ptr1 is not None:
                ptr1 = ptr1.next
            if ptr2 is not None:
                ptr2 = ptr2.next
        
        if carry != 0:
            rev_tail.next = ListNode(carry)
            rev_tail = rev_tail.next
        
        return rev_head
            
