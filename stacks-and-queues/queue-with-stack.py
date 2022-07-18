# https://leetcode.com/problems/implement-queue-using-stacks/description/

# Implement Queue using Stacks

# 1 <= x <= 9
# at most 100 calls will be made to push, pop, peek, and empty
# all the calls to pop and peek are valid



# oldest entered element is always at the top of stack2

class MyQueue:
    
    def __init__(self):
        self.inStack = []
        self.outStack = []

    
    # add elements to end of queue - "enqueue"
    def push(self, value):
        self.inStack.append(x)
            
    # remove element from front of queue and return it - "dequeue"
    def pop(self):
        moves = len(self.inStack) - 1
        for i in range(moves):
            self.outStack.append(self.inStack.pop())
        # leaves last item in first stack, which is the equivalent of the front of the queue
        removed_element = self.inStack.pop()
        # moving items back to inStack, sans removed element
        for i in range(moves):
            self.inStack.append(self.outStack.pop())
        return removed_element
    
    # returns element at front of the queue, or rather than last item in the stack array
    def peek(self):
        return self.inStack[0]
    
    # returns true if the queue is empty
    def empty(self):
        if len(self.inStack) == 0:
            return True
        else:
            return False
    
    