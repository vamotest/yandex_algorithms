
class MyQueue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def peek(self):
        if self.is_empty():
            return
        return self._items[0]


def solution(commands):
    stack = MyQueue()
    while commands:
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[0]))
        if command[0] == 'pop':
            print(stack.pop())
        if command[0] == 'size':
            print(stack.size())
        if command[0] == 'peek':
            print(stack.peek())
        commands -= 1


if __name__ == '__main__':
    solution(int(input()))
