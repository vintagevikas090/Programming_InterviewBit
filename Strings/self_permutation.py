'''
You are given two strings A and B.
Check whether there exists any permutation of both A and B such that they are equal.

Return a single integer 1 if its exists, 0 otherwise.



Problem Constraints
1 <= |A|, |B| <= 105
Both strings contain only lowercase english alphabets.


Input Format
The first argument is the string A. The second argument is the string B.


Output Format
Return a single integer 1 if a permutation exists, 0 otherwise.


Example Input
Input 1:
A = 'scaler'
B = 'relasc'
Input 2:

A = 'scaler'
B = 'interviewbit'


Example Output
Output 1:
1
Output 2:

0


Example Explanation
Explanation 1:
We can rearrange the second string to 'scaler', hence, a permuation exists.
Explanation 2:

The given length of the two strings itself is different. There is no possible permutation.
'''

from collections import Counter
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def permuteStrings(self, A, B):
        freq1 = Counter(A)
        freq2 = Counter(B)
        
        for char, freq in freq1.items():
            if freq2[char] != freq:
                return 0
        return 1
        
