
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
    
    def __str__(self):
        return self.value


def solution(node, value):
    index = 0
    while node:
        if node.value == value:
            return index
        node = node.next_item
        index += 1
    return -1
