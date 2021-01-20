
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
    
    def __str__(self):
        return self.value


def solution(node, idx):
    head = node
    
    if idx == 0:
        head = node.next_item
        return head
    
    while idx - 1:
        node = node.next_item
        idx -= 1
    
    node.next_item = node.next_item.next_item
    return head
