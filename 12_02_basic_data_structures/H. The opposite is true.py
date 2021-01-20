
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def solution(head):
    
    if head is None:
        return head

    head.next, head.prev = head.prev, head.next

    if head.prev is None:
        return head

    return solution(head.prev)
