'''
Given two binary strings A and B. Return their sum (also a binary string).


Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings



Input Format
The two argument A and B are binary strings.



Output Format
Return a binary string denoting the sum of A and B



Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output
Output 1:
"111"
Output 2:
"1000"


Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
 
The sum of 110 and 10 is 1000.
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        n, m = len(A), len(B)
        carry = 0
        result = []
    
        i, j = n-1, m-1
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                a_bit = int(A[i]) 
            else:
                a_bit = 0
                
            if j >= 0:
                b_bit = int(B[j]) 
            else:
                b_bit = 0
            
            total = a_bit + b_bit + carry
            
            result.append(str(total % 2))  
            carry = total // 2 
            
            i -= 1
            j -= 1
        
        # Since we added bits in reverse order, reverse the result to get the final binary sum
        return ''.join(result[::-1])
