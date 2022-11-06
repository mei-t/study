# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumber(l1, l2, 0)
    
    def addTwoNumber(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        current = ListNode()
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        n3 = carry
        s = n1 + n2 + n3
        current.val = s % 10
        if not l1 and not l2 and not carry:
            return None
        current.next = self.addTwoNumber(l1.next if l1 else l1, l2.next if l2 else l2, s // 10)
        return current

def createListNode(l: list[int], cur: int) -> ListNode:
    if cur >= len(l):
        return None
    curNode = ListNode(l[cur])
    curNode.next = createListNode(l, cur + 1)
    return curNode

def createListNodes(l: list[int]) -> ListNode:
    return createListNode(l, 0)

def printAns(l: ListNode) -> None:
    while l:
        print(l.val)
        l = l.next

if __name__ == "__main__":
    l1 = createListNodes([2, 4, 3])
    l2 = createListNodes([5, 6, 4])
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    printAns(result)