'''
You are given a string A, and you have to find all the amazing substrings of A.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
Note: Take the mod of the answer with 10003.


Problem Constraints
1 <= |S| <= 106
S can have special characters


Input Format
Only argument given is string S.


Output Format
Return a single integer X mod 10003, where X is the number of Amazing Substrings in the given string.


Example Input
ABEC


Example Output
6


Example Explanation
Amazing substrings of the given string are :
1. A
2. AB
3. ABE
4. ABEC
5. E
6. EC
here the number of substrings is 6 and 6 % 10003 = 6.

'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, string):
        if len(string) == 0:
            return 0
        
        vowel = 'aeiouAEIOU'
        vcount = 0
        tcount = 0
        
        for char in string:
            if char in vowel:
                # if first vowel
                if vcount == 0:
                    vcount = 1
                # else the substrings can be made from the all the vowels before
                else:
                    tcount += vcount
                    vcount += 1
            # if consonant -> substrings can be made from the all the vowels before
            else:
                tcount += vcount
                
        # since individual vowel is also a substring
        return (vcount + tcount) % 10003



# sol 2
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, string):
        n = len(string)
        if n == 0:
            return 0
        
        vowel = 'aeiouAEIOU'
        tcount = 0
        
        for i in range(n):
            if string[i] in vowel:
              # all the chars after the current vowel will contribute
                tcount = (tcount + n - i) % 10003
        
        return tcount 
