'''
Problem Description
 
 

You are given two numbers A and B.

You have to add them without using arithmetic operators and return their sum.



Problem Constraints
1 <= A, B <= 109


Input Format
The first argument is the integer A. The second argument is the integer B.


Output Format
Return a single integer denoting their sum.


Example Input
Input 1:
A = 3
B = 10
Input 2:

A = 6
B = 1


Example Output
Output 1:
13
Output 2:

7


Example Explanation
Explanation 1:
3 + 10 = 13
Explanation 2:

6 + 1 = 7.
Note, you have to add without using arithmetic operators.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def binary_sum(self, bin1, bin2):
        max_len = max(len(bin1), len(bin2)) 

        # Pad the shorter binary string with leading zeros
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)
        
        binA = bin1[::-1]
        binB = bin2[::-1]
        
        carry = 0
        res = []
        
        for i in range(len(binA)):
            val = int(binA[i]) + int(binB[i]) + carry
            bit = val % 2
            carry = val // 2
            res.append(str(bit))
            
        if carry != 0:
            res.append(str(carry))
        
        ans = ''.join(res[::-1])
        return ans
    
    
    def addNumbers(self, A, B):
        # Convert integers to binary strings (excluding the '0b' prefix)
        bin_a = bin(A)[2:]
        bin_b = bin(B)[2:]
        
        bin_sum = self.binary_sum(bin_a, bin_b)
        
        # binary to integer
        return int(bin_sum, 2)

