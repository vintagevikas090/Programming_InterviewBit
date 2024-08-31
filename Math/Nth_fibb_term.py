'''
Problem Description

Given an integer A you need to find the Ath fibonacci number modulo 109 + 7.

The first fibonacci number F1 = 1

The first fibonacci number F2 = 1

The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)



Problem Constraints
1 <= A <= 109.



Input Format
First argument is an integer A.



Output Format
Return a single integer denoting Ath fibonacci number modulo 109 + 7.



Example Input
Input 1:

 A = 4
Input 2:

 A = 3


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 F3 = F2 + F1 = 1 + 1 = 2
 F4 = F3 + F2 = 2 + 1 = 3
Explanation 2:

 F3 = F2 + F1 = 1 + 1 = 2

 '''

class Solution:
    # return f(n) and f(n+1)
    def fib(self, n):
      MOD = 10**9 + 7
        if n == 0:
            return (0, 1)
        else:
            # a = f(k) & b = f(k+1) -->> k = n // 2
            a, b = self.fib(n // 2) 
            # c = f(2k)
            c = (a * ((2 * b) - a)) % MOD
            # d = f(2k + 1)
            d = (a * a + b * b) % MOD
            
            if n % 2 != 0:
                return (d, (c + d) % MOD)
            else:
                return (c, d)

    def solve(self, A):
        # We return the first element of the tuple because
        # fib(A) returns (F(A), F(A+1))
        return self.fib(A)[0]
        
'''
The Fast Doubling formula for Fibonacci numbers is:
f(2k) = f(k) * [2 * f(k+ 1) - f(k)]        If n is even index
f(2k+ 1) = sq(f(k+1)) + sq(f(k))           If n is odd index

when n is even i.e n = 2k -> we have calculated f(2k)[c] and f(2k+1)[d] -> so return c and d
when n is odd i.e n = 2k+1 -> we have f(2k+1) only, we need f(2k+2)
and f(2k+2) --> f(2k) + f(2k+1) -> so return d and (c+d)

'''
