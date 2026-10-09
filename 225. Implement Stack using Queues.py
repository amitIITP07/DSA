class MyStack(object):

    def __init__(self):
        self.queue = deque()
        

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft() 

        

    def top(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue[0]    
        

    def empty(self):
        return len(self.queue)==0
