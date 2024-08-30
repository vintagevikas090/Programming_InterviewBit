'''
An integer interval [X, Y] (for integers X < Y) is a set of all consecutive integers from X to Y, including X and Y.

You are given a 2D array A with dimensions N x 2, where each row denotes an interval.

Find the minimum size of a set S such that for every integer interval Z in A, the intersection of S with Z has a size of at least two.



Problem Constraints
1 <= N <= 105
1 <= A[i][0] < A[i][1] <= 109


Input Format
The first argument is a 2D integer array A.


Output Format
Return a single integer denoting the minimum size of S.


Example Input
Input 1:
A = [[1, 3], [1, 4], [2, 5], [3, 5]]
Input 2:

A = [[1, 2], [2, 3], [2, 4], [4, 5]]


Example Output
Output 1:
3
Output 2:

5


Example Explanation
Explanation 1:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Explanation 2:

An example of a minimum sized set is {1, 2, 3, 4, 5}.

'''

  class Solution:
    # @param A : list of list of integers
    # @return an integer
    def setIntersection(self, A):
        n = len(A)
        A.sort(key=lambda x: x[1])
        res = []
        res.append(A[0][1] - 1)
        res.append(A[0][1])
        for i in range(1, n):
            start = A[i][0]
            end = A[i][1]
            last = res[-1]
            secondLast = res[-2]
            if (start > last):
                res.append(end - 1)
                res.append(end)
            elif (start == last):
                res.append(end)
            elif (start > secondLast):
                res.append(end)
        return len(res)

'''
Case 1: If the start of the interval is greater than last (i.e., start > last):
    This means the current interval is not covered by the last two points in res.
    To cover this interval, the solution adds two points: end - 1 and end to res.
Case 2: If the start of the interval is equal to last (i.e., start == last):
    This means the interval is only partially covered by last, so one more point (end) 
    is added to fully cover it.
Case 3: If the start of the interval is greater than secondLast but less than or equal to last:
    This means the interval is partially covered by secondLast, so one more point (end) 
    is added to ensure full coverage.
'''
