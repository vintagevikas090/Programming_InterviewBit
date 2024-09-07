'''
Problem Description

Given a linked list A of length N and an integer B.

You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

If no such element exists, then return -1.

NOTE:

Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.


Problem Constraints
1 <= N <= 105
1<= Value in Each Link List Node <= 103
1 <= B <= 105


Input Format
First argument is the head pointer of the linkedlist A.

Second argument is an integer B.



Output Format
Return an integer denoting the value of the Bth from the middle towards the head of the linked list A. If no such element exists, then return -1.



Example Input
Input 1:

 A = 3 -> 4 -> 7 -> 5 -> 6 -> 1 6 -> 15 -> 61 -> 16
 B = 3
 Input 2:

 A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
 B = 2
 Input 3:

 A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
 B = 10
 '''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    
    def solve(self, head, k):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        target_position = (length // 2) + 1 - k

        if target_position <= 0 or target_position > length:
            return -1
            
        temp = head
        i = 1
        while temp is not None:
            if i == target_position:
                return temp.val
            i += 1
            temp= temp.next

        return -1
