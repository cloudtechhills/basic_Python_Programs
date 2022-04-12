#THIS PROGRAM CREATES MY QUEUE WRAPPER CLASS
from collections import deque


class Queue():
    
    """LAST IN FIRST OUT"""
    def __init__(self):
        self.queue = deque()
    
    def __str__(self):
        return str(self.queue)


    #ADD ITEM TO THE LIST
    def push(self, item):
        return self.queue.append(item)

    
    #ADD ITEM TO THE QUEUE LIST FROM THE LEFT-HAND SIDE
    def push_left(self, item):
        return self.queue.appendleft(item)
        
    
    #REMOVE AN ITEM FROM THE LIST
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None

    #REMOVE AN ITEM FROM THE LEFT-HAND SIDE
    def pop_left(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None


    #SEE THE LAST ITEM IN THE LIST
    def peek(self):
        if len(self.queue ) > 0:
            return self.queue[len(self.queue)-1]
        else:
            return None

        
if __name__ == "__main__":
    start = Queue()
    start.push('Hello')
    start.push_left('Francis')
    print(start.__str__())