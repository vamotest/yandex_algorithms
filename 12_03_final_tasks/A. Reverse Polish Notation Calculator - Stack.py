
# https://contest.yandex.ru/contest/18357/run-report/45731081/

import operator

ACTIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:
    def __init__(self):
        self._items = []
    
    def __bool__(self):
        return bool(self._items)
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if not self:
            raise IndexError('The stack is empty')
        return self._items.pop()
    
    def peak(self):
        if not self:
            raise IndexError('The stack is empty')
        return self._items[-1]


def calculate(data):
    stack = Stack()
    for element in data:
        if element not in ACTIONS:
            stack.push(int(element))
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()
            stack.push(
                ACTIONS[element](first_operand, second_operand)
            )
    return stack.peak()


def main():
    expression_list = input().split()
    print(calculate(expression_list))


if __name__ == '__main__':
    main()
