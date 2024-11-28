class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head
        fast = fast.next
        while slow and fast and fast.next:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
# work on exceeded time limit error 