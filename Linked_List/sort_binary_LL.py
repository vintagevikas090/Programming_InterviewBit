'''
Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

Try to do it in constant space.


Problem Constraints
 1 <= N <= 105

 A.val = 0 or A.val = 1



Input Format
First and only argument is the head pointer of the linkedlist A.



Output Format
Return the head pointer of the new sorted linked list.



Example Input
Input 1:

 1 -> 0 -> 0 -> 1
Input 2:

 0 -> 0 -> 1 -> 1 -> 0


Example Output
Output 1:

 0 -> 0 -> 1 -> 1
Output 2:

 0 -> 0 -> 0 -> 1 -> 1


Example Explanation
Explanation 1:

 The sorted linked list looks like:
  0 -> 0 -> 1 -> 1
Explanation 2:

 The sorted linked list looks like:
  0 -> 0 -> 0 -> 1 -> 1


'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, head):
        if head is None or head.next is None:
            return head
        count_0, count_1 = 0, 0
        current = head
        while current:
            if current.val == 0:
                count_0 += 1
            else:
                count_1 += 1
            current = current.next

        # Update the values of the nodes based on counts
        current = head
        while current:
            if count_0 > 0:
                current.val = 0
                count_0 -= 1
            else:
                current.val = 1
                count_1 -= 1
            current = current.next

        return head
