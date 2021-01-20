
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


class StackMax(Stack):
    
    def pop(self):
        if not self.items:
            print('error')
            return
        else:
            return super().pop()
            
    def get_max(self):
        if not self.items:
            return None
        return max(self.items)


def solution(commands):
    stack = StackMax()
    
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
