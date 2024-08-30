'''
Problem Description
 
 

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.

Return the final order of the logs.


Problem Constraints
1 <= logs.length <= 1000
3 <= logs[i].length <= 1000
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.


Input Format
The first argument is a string array A where each element is a log.


Output Format
Return the string array A after making the changes.


Example Input
Input 1:
A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
Input 2:

A = ["a1-9-2-3-1","g1-act-car","zo4-4-7","ab1-off-key-dog","a8-act-zoo"]


Example Output
Output 1:
["let1-art-can","let3-art-zero","let2-own-kit-dig","dig1-8-1-5-1","dig2-3-6"]
Output 2:

["g1-act-car", "a8-act-zoo", "ab1-off-key-dog", "a1-9-2-3-1", "zo4-4-7"]
'''

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def reorderLogs(self, A):
        def is_digit_log(log):
            log_info = log.split("-", 1)[1]
            # if log_info has digits -> return true
            if log_info[0].isdigit():
                return True
            else:
                return False
       
        def log_key(log):
            identifier, content = log.split("-", 1)
            return (content, identifier)
       
        letter_logs = []
        digit_logs = []
       
        for log in A:
            if is_digit_log(log):
                digit_logs.append(log)
            else:
                letter_logs.append(log)
       
       
        '''Apply log_key to Each Log:
            For each log in letter_logs, log_key(log) is called.
            This converts each log into a tuple (content, identifier).
            so sorting will be done based of 1st ele of tuple -> i.e content
        '''
        letter_logs.sort(key=log_key)
        return letter_logs + digit_logs
        

'''
.split('-', 1) -> splits the string at first hyphen
so it retrun list of 2 ele: one before 'first' hyphen and one after first hyphen
'''
