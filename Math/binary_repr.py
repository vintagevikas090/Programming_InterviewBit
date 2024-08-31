'''
Given a number N >= 0, find its representation in binary.

Example:

if N = 6,

binary form = 110
'''
class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A == 0:
            return '0'
        ret = ''
        while A != 0:
            ret += str(A%2)
            A /= 2
        return ret[::-1]
