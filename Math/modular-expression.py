'''
Implement pow(A, B) % C.
In other words, given A, B and C, find (AB)%C. 



Problem Constraints
-106 <= A <= 109
0 <= B <= 109
0 <= C <= 109


Input Format
The first argument is an integer A.
The second argument is an integer B.
The third argument is an integer C.


Output Format
Return an integer equal to (AB) % C


Example Input
A = 2, B = 3, C = 3


Example Output
2


Example Explanation
2^3 % 3 = 8 % 3 = 2
'''


class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @return an integer
	def Mod(self, A, B, C):
		if C == 0 or A == 0:
			return 0
		if B == 0:
			return 1

		half_pow = (self.Mod(A, B//2, C)) % C   # A^(B//2) % C 
		
		if B % 2 == 0:
			return (half_pow * half_pow) % C
		else:
			return ((half_pow * half_pow) % C) * A % C 
			
			
			
			
# Concept about multiplication property of modulus
# (x * y) % c == [ (x % c) * (y % c) ] % c 


# for B = even -> we need 
# 		(A pow B)% c = (A pow(B//2) * A pow(B//2)) % c 
# for B = odd -> we need 
# 		(A pow B) % c = (A * A pow(B//2) * A pow(B//2)) % c 
