'''
 Given a string A with lowercase english alphabets and you have to return a string in which, with each character its frequency is written in adjacent.



Problem Constraints
1 <= |A| <= 105


Input Format
First argument is the string A with lowercase english alphabets.


Output Format
Return a string in which each character frequency is written in adjacent.


Example Input
Input 1:
abbhuabcfghh
Input 2:

a


Example Output
Ouput 1:
a2b3h3u1c1f1g1
Ouput 2:

a1


Example Explanation
Explanation 1:
‘a’ occurs in the string a total of 2 times so we write a2 then ‘b’ occurs a total of 3 times so next we write b3 and so on
Explanation 2:

‘a’ occurs in the string a total of 1 time only.
'''


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        freq = {}
        for char in A:
            freq[char] = freq.get(char, 0) + 1
            
        result = ''
        for char, fr in freq.items():
            result = result + char + str(fr)
        return result
