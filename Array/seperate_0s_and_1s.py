'''
Segregate 0s and 1s in an array
Programming
Arrays
medium
77.2% Success

125

18

Bookmark
Asked In:
Problem Description
 
 


You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. Traverse array only once. 



Problem Constraints
1<=|A|<=1e6


Input Format
First argument is array of integers consisting of 0's and 1's only.


Output Format
Return a sorted array.


Example Input
Input 1:
a=[0 1 0]
Input 2:

A=[1 1 0 ]


Example Output
Ouput 1:
[0 0 1]
Ouput 2:

[0 1 1]


Example Explanation
Explanation 1:
 above is sorted array.
Explanation 2:

sort the array.

'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        s = sum(A)
        l = len(A)
        zeros, ones = (l - s), s 
        for i in range(l):
            if zeros > 0:
                A[i] = 0
                zeros -= 1
            else:
                A[i] = 1
        
        return A  
