'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.


Q: What should pop do on empty stack? 
A: In this case, nothing. 



Q: What should top() do on empty stack?
A: In this case, return -1

NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
'''

class MinStack:

    def __init__(self):
        self.stack = []     
        self.min_stack = []  

    # each time we append, take care of the min val
    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0 or  val <= self.min_stack[-1]:
            self.min_stack.append(val)
            # Hence min ele will be top ele of min_stack
  
    # each time we pop, check whether it is min ele
    def pop(self):
        if len(self.stack) == 0:
            return 
        temp = self.stack.pop()
        if temp == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1]

    def getMin(self):
        if len(self.min_stack) == 0:
            return -1
        return self.min_stack[-1]
