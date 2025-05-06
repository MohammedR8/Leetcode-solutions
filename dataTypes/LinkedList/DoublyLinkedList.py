class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        
        while last.next:
            last = last.next
        new_node.prev = last
        last.next = new_node
        
    def insert(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be null")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    

    def delete_node(self, key):
        current_node = self.head
        prev_node = None

        # Special case: deleting the head node
        if current_node and current_node.data == key:
            if current_node.next:
                current_node.next.prev = None
            self.head = current_node.next
            return

        # Traverse to find the node
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        # Key not found
        if not current_node:
            return

        # Delete current_node
        prev_node.next = current_node.next

        if current_node.next:
            current_node.next.prev = prev_node



    def find_node(self,key):
        current = self.head
        
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    