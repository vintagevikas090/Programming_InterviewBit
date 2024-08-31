# find all prime no upto A (A included)

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
        
    def sieve(self, A):
        if A == 1:
            return []
        output = []
        for i in range(2, A+1):
            if self.isPrime(i) == 1:
                output.append(i)
        return output
