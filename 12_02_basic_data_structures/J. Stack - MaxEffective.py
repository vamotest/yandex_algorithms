
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
    

class StackMaxEffective(Stack):

    def __init__(self):
        super().__init__()
        self.max_items = []
        
    def push(self, item):
        if self.max_items and self.max_items[-1] <= item:
            self.max_items.append(item)
        if not self.max_items:
            self.max_items.append(item)
        return super().push(item)

    def pop(self):
        if self.is_empty():
            print('error')
            return
        else:
            item = super().pop()
            if self.max_items[-1] == item:
                self.max_items.pop()

    def get_max(self):
        if self.is_empty():
            return None
        return self.max_items[-1]


def solution(commands):
    stack = StackMaxEffective()
    
    for _ in range(commands):
        command = input()
        
        if command == 'get_max':
            print(stack.get_max())
        elif command == 'pop':
            stack.pop()
        else:
            stack.push(int(command.split()[-1]))


if __name__ == '__main__':
    solution(int(input()))
