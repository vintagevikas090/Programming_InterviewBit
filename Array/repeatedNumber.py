'''
Input Format
The first argument is an integer array A.


Output Format
Return the integer that repeats in array A


Example Input
Input 1:
A = [3, 4, 1, 4, 2]
Input 2:
A = [1, 2, 3]
Input 3:
A = [3, 4, 1, 4, 1]


Example Output
Output 1:
4
Output 2:
-1
Output 3:
1


Example Explanation
Explanation 1:
4 repeats itself in the array [3, 4, 1, 4, 2]
Explanation 2:
No number repeats itself in the array [1, 2, 3]
Explanation 3:
1 and 4 repeats itself in the array [3, 4, 1, 4, 1], we can return 1 or 4
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        # freq = {}
        # for val in A:
        #     freq[val] = freq.get(val, 0) + 1
        
        # v = -1
        # for i in freq:
        #     if freq[i] > 1:
        #         v = i 
        # return v
        
        freq = {}
        for val in A:
            if val in freq:
                return val
            else:
                freq[val] = 1
        
        return -1
