'''
Implement pow(x, n) % d.
In other words, given x, n and d,
Find (xn % d)
Note that remainders on division cannot be negative. In other words, make sure the answer you return is non-negative integer.


Problem Constraints
-109 <= x <= 109
0 <= n <= 109
1 <= d <= 109


Example Input
Input 1:
x = 2
n = 3
d = 3
Input 2:
x = 5
n = 2
d = 6


Example Output
Output 1:
2
Output 2:
1


Example Explanation
Explanation 1:
23 % 3 = 8 % 3 = 2.
Explanation 2:
52 % 6 = 25 % 6 = 1.
'''

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    
    def pow(self, x, n, d):
        if d == 1:
            return 0
        if n == 0:
            return 1
        
        half = self.pow(x, n // 2, d)
        val = (half * half)
        
        if n % 2 == 1:
            return (val * x) % d
        else:
            return val % d
