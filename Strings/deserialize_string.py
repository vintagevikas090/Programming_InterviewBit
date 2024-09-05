'''
You are given a string A which is a serialized string. You have to restore the original array of strings.

The string in the output array should only have lowercase english alphabets.

Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.

For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.



Problem Constraints
1 <= |A| <= 106


Input Format
The first argument is the string A.


Output Format
Return an array of strings which are deserialized.


Example Input
Input 1:
A = 'scaler6~academy7~'
Input 2:

A = 'interviewbit12~'


Example Output
Output 1:
['scaler', 'academy']
Output 2:

['interviewbit']


Example Explanation
Explanation 1:
Length of 'scaler' is 6 and academy is 7. So, the resulting string is scaler6~academy7~.
We hve to reverse the process.
Explanation 2:

Explained in the description above.
'''

class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        deserialized = []
        i = 0
        n = len(A)
        
        while i < n:
            # getting the string starting from i
            j = i
            while A[j].isalpha():
                j += 1
            string_part = A[i:j]
            
            # skip the len part from A 
            # get the len (in case str len is more the one digit)
            # start is from 'j' becz prev string ended at this 'j'
            length_start = j
            while A[j].isdigit():
                j += 1
            
            # skipping the '~'
            j += 1
            
            deserialized.append(string_part)
            i = j
        
        return deserialized
