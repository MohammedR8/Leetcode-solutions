from stacks import Stack
from queues import Queues


def reverseString(str):
    stack = Stack()
    sortedString = []

    for string in str:
        stack.push(string)
        
    while not stack.is_empty():
        sortedString.append(stack.pop())


    return sortedString


def sortStack(orgStack):
    stack1 = Stack()
    stack2 = Stack()
    len = orgStack.size()



    for i in range (len):
        num = orgStack.pop()
        
        while (not stack1.is_empty()) and (num < stack1.peek()):
            temp = stack1.pop()
            stack2.push(temp)
        stack1.push(num)

        while not stack2.is_empty():
            temp2 = stack2.pop()
            stack1.push(temp2)




    return stack1


# stack = Stack()
# for item in [3, 1, 4, 2]:
#     stack.push(item)

# print(sortStack(stack).items)
















    

    
     