'''
Problem Description
 
 

Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.

Check the sample test case for reference.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem


Problem Constraints
1 <= |A| <= 106


Input Format
The first argument is a string A.


Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem


Example Input
Input 1:
"A man, a plan, a canal: Panama"
Input 2:
"race a car"


Example Output
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
The input string after ignoring spaces, and all special characters is "AmanaplanacanalPanama" 
which is a palindrome after ignoring the case.
Explanation 2:
The input string after ignoring spaces, and all special characters is "raceacar" which is not a palindrome
'''

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, string):
        if len(string) == 0 or len(string) == 1:
            return 1
        
        left, right = 0, len(string)-1
        while left < right:
            if string[left].isalnum() and string[right].isalnum():
                if string[left].lower() != string[right].lower():
                    return 0
                left += 1
                right -= 1
            
            if not string[left].isalnum():
                left += 1
            if not string[right].isalnum():
                right -= 1
                
        return 1
            
