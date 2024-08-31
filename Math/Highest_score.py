'''
Problem Description
 
 

You are given a 2D string array A of dimensions N x 2,

where each row consists of two strings: first is the name of the student, second is their marks.

You have to find the maximum average mark. If it is a floating point, round it down to the nearest integer less than or equal to the number.



Problem Constraints
1 <= N <= 105


Input Format
The first argument is a 2D string array A.


Output Format
Return a single integer which is the highest average mark.


Example Input
Input 1:
A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"]]
Input 2:

A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"], ["Alice", "10"]]


Example Output
Output 1:
90
Output 2:

85


Example Explanation
Explanation 1:
Alice has the highest average with 90 marks.
Explanation 2:

Bob has the highest average with 85 marks.
'''

class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, arr):
        d = {}
        for name, marks in arr:
            marks = int(marks)
            if name not in d:
                d[name] = (1, marks)
            else:
                freq = d[name][0]
                curr_marks = d[name][1]
                new_marks = curr_marks + marks
                d[name] = (freq+1, new_marks)
        
        
        max_avg = -10000000
        for val in d.items():
            name = val[0]
            info = val[1]
            avg = info[1] / info[0]
            if avg > max_avg:
                max_avg = avg
                
        return int(max_avg)
