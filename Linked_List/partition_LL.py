'''
 Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B. 

 You should preserve the original relative order of the nodes in each of the two partitions. 



Problem Constraints
 1 <= |A| <= 106 

 1 <= A[i], B <= 109 



Input Format
 The first argument of input contains a pointer to the head to the given linked list. 

 The second argument of input contains an integer, B. 



Output Format
 Return a pointer to the head of the modified linked list. 



Example Input
 Input 1: 

A = [1, 4, 3, 2, 5, 2]
B = 3
 Input 2: 

A = [1, 2, 3, 1, 3]
B = 2


Example Output
 Output 1: 

[1, 2, 2, 4, 3, 5]
 Output 2: 

[1, 1, 2, 3, 3]


Example Explanation
Explanation 1:

 [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
Explanation 2:

 [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.
 '''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, head, B):
        if head is None or head.next is None:
            return head
        
        less_than_B, ptr1 = None, None
        greater_than_B, ptr2 = None, None
        
        temp = head
        while temp is not None:
            next_node = temp.next
            temp.next = None
            if temp.val < B:
                if less_than_B is None:
                    less_than_B = temp
                    ptr1 = temp
                else:
                    ptr1.next = temp
                    ptr1 = ptr1.next
            else:
                if greater_than_B is None:
                    greater_than_B = temp
                    ptr2 = temp
                else:
                    ptr2.next = temp
                    ptr2 = ptr2.next
            temp = next_node
            
        if less_than_B and greater_than_B:
            ptr1.next = greater_than_B
            return less_than_B
        elif less_than_B is None:
            return greater_than_B
        elif greater_than_B is None:
            return less_than_B
        else:
            return None
        
