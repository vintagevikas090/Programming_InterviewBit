'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.



Problem Constraints
1 <= |A| <= 106


Input Format
The first argument is a string A


Output Format
Return an integer denoting the length of the last word in the string.


Example Input
Input 1:
A = " hello world "
Input 2:
A = "InterviewBit"


Example Output
Output 1:
5
Output 2:
12


Example Explanation
Explanation 1:
"world" is the last word of size 5
Explanation 2:
"InterviewBit" is the last word of size 12
'''

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, string):
        n = len(string)
        i = n - 1
        
        # skipping the spaces
        while i >= 0 and string[i] == ' ':
            i -= 1
            
        # counting the len of last word 
        length = 0
        while i >= 0 and string[i] != ' ':
            length += 1
            i -= 1
        
        return length



# using inbuilt funtions
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, string):
        string = string.strip()
        if len(string) == 0:
            return 0
        data = string.split()
        return len(data[-1])



