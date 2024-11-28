'''
Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Problem Constraints
0 <= sum of length of all strings <= 1000000



Input Format
The only argument given is an array of strings A.



Output Format
Return the longest common prefix of all strings in A.



Example Input
Input 1:

A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];


Example Output
Output 1:

"a"
Output 2:

"ab"


Example Explanation
Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".
'''


class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        if len(A) == 0:
            return ''
        
        prefix = A[0]
        
        for s in A[1:]:
            # if 's is not starting with prefix' -> reduce prefix size
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                
                # if prefix becmoes '' -> no common prefix 
                if len(prefix) == 0:
                    return ''
        return prefix
