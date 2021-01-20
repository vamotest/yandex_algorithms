
class MyQueue:
    def __init__(self, max_queue):
        self._items = []
        self.max_queue = max_queue
        self.size_queue = 0
    
    def is_empty(self):
        return self._items == []
    
    def push(self, item):
        if self.size_queue != self.max_queue:
            self._items.append(item)
            self.size_queue += 1
        else:
            print('error')
    
    def pop(self):
        if self.is_empty():
            return None
        self.size_queue -= 1
        return self._items.pop(0)
    
    def size(self):
        return self.size_queue
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self._items[0]
        

def solution(commands, max_queue):
    stack = MyQueue(max_queue)
    while commands:
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            print(stack.pop())
        if command[0] == 'size':
            print(stack.size())
        if command[0] == 'peek':
            print(stack.peek())
        commands -= 1
    
    
if __name__ == '__main__':
    solution(int(input()), int(input()))



