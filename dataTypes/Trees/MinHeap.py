
class MinHeap:
        def __init__(self,items):
            if items:
                self.heap = items
            else:
                self.heap = []


        def push(self, val):
            self.heap.append(val)
            self._bubble_up(len(self.heap)-1)


        def _bubble_up(self,idx):
            parent = self._parent(idx)
            
            while parent > 0 and self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
                parent = self._parent(idx)
             
        
        def pop(self):
            if len(self.heap) == 0:
                return None
            elif len(self.heap) == 1:
                return self.heap.pop()
            
            min = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self._bubble_down(0)

            return min


        def _bubble_down(self, idx):
            min = idx
            left = self._left_child(idx)
            right = self._right_child(idx)

            if left < len(self.heap) and self.heap[min] > self.heap[left]:
                min = left
            if right < len(self.heap) and self.heap[min] > self.heap[right]:
                min = right

            if min != idx:
                self.heap[idx], self.heap[min] = self.heap[min], self.heap[idx]
                self._bubble_down(min)

            
             
             
        
        def peek(self):
            if len(self.heap) < 1:
                return None
            return self.heap[0]
    

        def _parent(self , idx):
            return (idx -1) // 2

        def _left_child(self, idx):
            return 2 * idx + 1
        
        def _right_child(self, idx):
            return 2 * idx + 2