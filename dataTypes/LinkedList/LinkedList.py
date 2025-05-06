class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node
        
        
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.value == key:
            self.head = current_node.next
            current_node = None
            return
        
        prev_node = None
        while current_node and current_node.value !=key:
            prev_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return
    
        prev_node.next = current_node.next
        
        current_node = None
        
        
        
        
        
    def insert_node(self, value, prev_node):
        
        if not prev_node:
            print("The given previous node must be in the LinkedList")
            return
        
        node = Node(value)
        
        node.next = prev_node.next
        
        prev_node.next = node
        
        
        
    def find_node(self, key):
        
        current_node = self.head
        
        if current_node and current_node.value == key:
            return current_node
            
        while current_node and current_node.value != key:
            current_node = current_node.next
            
        if current_node is None:
            return -1
        return current_node
        
        
    def get(self, index):
        if index<0:
            return None
        
        count = 0
        current_node = self.head
        
            
        while current_node:
            if count == index:
                return current_node.value
            count += 1 
            current_node = current_node.next

        return None
        

    def reverse(head):
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

        
        
        
        
            
            
            
            
            
            
            
            
            