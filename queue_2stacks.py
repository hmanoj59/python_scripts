class Stack2():

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)
    def dequeu(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
                
