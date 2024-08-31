'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.
If there is more than one solution possible, return the lexicographically smaller solution i.e.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 
If a < c OR ( a == c AND b < d ).
NOTE: A solution will always exist. read Goldbach's conjecture


Problem Constraints
1 <= A <= 2 * 107


Input Format
The first argument is an integer A.


Output Format
Return an array of integers.


Example Input
4


Example Output
[2, 2]


Example Explanation
2 + 2 equals 4, which is the lexicographically smaller solution
'''



# sol 1 -> uses more memory
class Solution:
    # @param A : integer
    # @return a list of integers
    def get_primes_upto_n(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        i = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        return is_prime  
    
    def primesum(self, A):
        prime_nums = self.get_primes_upto_n(A)
        for num in range(2, A + 1):
            if prime_nums[num]:
                num2 = A - num
                if num2 >= num and prime_nums[num2]:
                    return [num, num2]



# sol2 -> TC = O(n square)

class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, A):
        if A == 1:
            return 0
        limit = int(A ** 0.5)
        for i in range(2, limit+1):
            if A % i == 0:
                return 0
        return 1    
    
    def primesum(self, A):
        for num in range(2, A + 1):
            check1 = self.isPrime(num)
            check2 = self.isPrime(A - num)
            
            if check1 == 1 and check2 == 1:
                return [num, num2]


# sol3 -> most optimal
class Solution:
    # @param A : integer
    # @return a list of integers
    import math

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        # since prime no > 3 can be written in form { 6K(+-)1 }
        i = 5 # k = 1
        # check divisibility be 6k+-1
        while i * i <= n:
            # i -> 6k- 1      # i+2 -> 6k+1
            if n % i == 0 or n % (i + 2) == 0:
                return False
            # inc by 6 -> k will become +1
            i += 6
        return True

    def primesum(self, A):
        for num1 in range(2, A // 2 + 1):
            check1 = self.is_prime(num1)
            num2 = A - num1
            check2 = self.is_prime(num2)
            if num1 <= num2 and check1 and check2:
                return [num1, num2]
