
class Stack:
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


class StackSet(Stack):
    
    def __init__(self):
        super().__init__()
        self.items_set = set()
    
    def push(self, item):
        if item not in self.items_set:
            self.items_set.add(item)
            return super().push(item)
    
    def pop(self):
        if self.is_empty():
            print('error')
            return
        else:
            item = super().pop()
            self.items_set.remove(item)
    
    def peek(self):
        if self.is_empty():
            return 'error'
        else:
            return super().peek()


def solution(commands):
    stack = StackSet()
    
    for _ in range(commands):
        command = input()
        
        if command == 'peek':
            print(stack.peek())
        elif command == 'pop':
            stack.pop()
        elif command == 'size':
            print(stack.size())
        else:
            stack.push(int(command.split()[-1]))


if __name__ == '__main__':
    solution(int(input()))
