
# https://contest.yandex.ru/contest/18357/run-report/45413536/

def hasCycle(head):
    
    slow, fast = head, head
    while (fast and fast.next) is not None:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            return True

    return False
