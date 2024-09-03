'''
Given a string A consisting of lowercase characters.

You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.

Return the count of substring modulo 109 + 7.



Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.



Input Format
First argument is an string A.



Output Format
Return a integer denoting the the number of substrings in A which starts with vowel and end with consonants or vice-versa with modulo 109 + 7.



Example Input
Input 1:

 A = "aba"
Input 2:

 A = "a"


Example Output
Output 1:

 2
Output 2:

 0


Example Explanation
Explanation 1:

 Substrings of S are : [a, ab, aba, b, ba, a]Out of these only 'ab' and 'ba' satisfy the condition for special Substring. So the answer is 2.
Explanation 2:

 No possible substring that start with vowel and end with consonant or vice-versa.
 '''

class Solution:
    # @param A : string
    # @return an integer

    # sol1 -> not Optimal
    def starts_with_vowels(self, st):
        vowel = 'aeiou'
        return st[0] in vowel
    
    def ends_with_consonents(self, st):
        consonents = 'bcdfghjklmnpqrstvwxyz'
        return st[-1] in consonents
    
    def satisfy_condition(self, st):
        return (self.starts_with_vowels(st) and self.ends_with_consonents(st)) or \
                (not self.starts_with_vowels(st) and not self.ends_with_consonents(st))
    
    
    def solve(self, string):
        n = len(string)
        if n == 0 or n == 1:
            return 0
        count = 0
        for i in range(n):
            s = ''
            for j in range(i, n):
                s += string[j]
                if self.satisfy_condition(s):
                    count += 1
        return count
        
        
        
        
    def solve(self, string):
        n = len(string)
        mod = 10**9 + 7 
        if n == 0 or n == 1:
            return 0
        vowel = 'aeiou'
        vowel_count, cons_count, ans = 0, 0, 0
        for char in string:
            if char in vowel:
                ans += cons_count
                vowel_count += 1
            else:
                ans += vowel_count
                cons_count += 1
                
        return ans % mod
        
'''
When You Encounter a Vowel:

Every time you find a vowel at position i, all the previous substrings that start with
a consonant and end just before i can form a new valid substring with the current vowel.
Add the current consonant_count to total_count.
Then, increment vowel_count because this character could start a new substring
that might be valid when combined with future consonants.
  
Same goes for consonants
'''
