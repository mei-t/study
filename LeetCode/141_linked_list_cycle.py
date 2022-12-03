from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# TC: O(n)
# SC: O(n)
# 6:50
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = set()
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        
        return False

# TC: O(n)
# SC: O(1)
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True