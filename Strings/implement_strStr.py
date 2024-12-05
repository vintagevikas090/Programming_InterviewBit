'''
Implement strStr().

strstr - locate a substring ( needle ) in a string ( haystack ).

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

NOTE: String A is haystack, B is needle.


Input Format
The first argument is a string A (haystack)
The second argument is a string B (needle)


Output Format
Return an integer, the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example Input
Input 1:
A = "strstr"
B = "str"
Input 2:
A = "bighit"
B = "bit"


Example Output
Output 1:
0
Output 1:
-1


Example Explanation
Explanation 1:
"str" occurs at index 0 and 3.
The first occurrence is at index 0, so we return 0.
Explanation 2:
"bit" did not occur in "bighit", so we return -1.

'''


class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def strStr(self, A, B):
		if(B not in A):
            	     return -1
			
	        l=len(B)
	        for i in range(len(A)-l+1):
	            if(A[i:i+l]==B):
	                return i
