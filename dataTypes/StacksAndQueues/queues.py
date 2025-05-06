class Queues:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.popleft()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items=[]

    def contain(self, item):
        return item in self.items

    def reverse(self):
        self.items.reverse()



