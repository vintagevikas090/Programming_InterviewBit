'''
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124

'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 0:
            return []
            
        # count no of zeros before most significant digit
        cnt = 0
        for val in A:
            if val == 0:
                cnt += 1
            # once non zero val encounterd, stop 
            if val != 0:
                break
        # if all val is zero
        if cnt == len(A):
            return [1]
        newA = A[cnt:]
        
        # reverse the array
        arr = newA[::-1]
        n = len(arr)
        result, carry = [], 0
        
        for i in range(n):
            val = arr[i] + carry
            if i == 0:
                val += 1
            digit = val % 10 
            carry = val // 10
            result.append(digit)
        
        if carry != 0:
            result.append(carry)
            
        return result[::-1]