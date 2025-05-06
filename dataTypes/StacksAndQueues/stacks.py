# Import the LinkedList class from the LinkList.py file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LinkedList.LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
            
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
            
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return len(self.items) == 0
        
    def clear(self):
        self.items = []
        
    def to_list(self):
        # Create a linked list
        linked_list = LinkedList()
        # Traverse the stack from the top to the bottom
        for i in range(len(self.items)-1, -1, -1):
            linked_list.append(self.items[i])  # Append each element to the linked list
        return linked_list
