'''
You are given a array of strings A of length N.

You have to return another string array which contains all possible special strings in Lexicographic order.
 A special string is defined as a string with length equal to N, 
 and ith character of the string is equal to any character of the ith string in the array A.



Problem Constraints
1 <= N <= 5
1 <= |Ai| <= 8


Input Format
The first argument is the string array A.


Output Format
Return a string array consisting of all possible special strings.


Example Input
Input 1:
A = ['ab', 'cd']
Input 2:

A = ['aa', 'bb']


Example Output
Output 1:
['ac', 'ad', 'bc', 'bd']
Output 2:

['ab', 'ab', 'ab', 'ab']


Example Explanation
Explanation 1:
Since, the first character has to be from the 1st string 'ab' and the 2nd from 'cd'.
These are the all possible 4 combinations.
Explanation 2:

Note we can have duplicate strings, you have to add all of them.'

'''

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def specialStrings(self, A):
        from itertools import product
        
        A = [sorted(string) for string in A]
        
        combinations = product(*(st for st in A))
        
        res = []
        for pair in combinations:
            res.append(''.join(pair))
            
        return res


# product(* (iterable) ) -> generates all possible combination out of the iterable
# eg. for ['ab', 'cd'] ->> [(a, c), (a,d), (b,c), (b,d)]
      
