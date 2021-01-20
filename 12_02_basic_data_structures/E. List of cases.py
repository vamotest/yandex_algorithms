
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
    
    def __str__(self):
        return self.value


def solution(node):
    print(node.value)
    while node.next_item:
        node = node.next_item
        print(node.value)
