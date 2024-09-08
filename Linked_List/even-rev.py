'''
Given a linked list A , reverse the order of all nodes at even positions.



Problem Constraints
1 <= Size of linked list <= 100000



Input Format
First and only argument is the head of the Linked-List A.



Output Format
Return the head of the new linked list.



Example Input
Input 1:

A = 1 -> 2 -> 3 -> 4
Input 2:

A = 1 -> 2 -> 3


Example Output
Output 1:

 1 -> 4 -> 3 -> 2
Output 2:

 1 -> 2 -> 3


Example Explanation
Explanation 1:

Nodes are positions 2 and 4 have been swapped.
Explanation 2:

No swapping neccassary here.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, head):
        if not head or not head.next: 
            return head
        
        # Separate even and odd nodes
        odd_head = head
        even_head = head.next
        even = even_head
        odd = odd_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = None # imp to break the odd and even part
        
        
        # Reverse the even part
        prev, curr = None, even_head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        even_head = prev 
        
        # Merge the odd and rev even parts
        odd = odd_head
        even = even_head
        while even:
            next_odd = odd.next
            next_even = even.next
            odd.next = even
            even.next = next_odd
            odd = next_odd
            even = next_even
        
        return odd_head
