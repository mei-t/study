# https://leetcode.com/problems/add-two-numbers/
# 10:27

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
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

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        cur = dummyHead
        carry = 0
        while l1 or l2 or carry > 0:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            s = n1 + n2 + carry
            nextNode = ListNode(s % 10)
            carry = s // 10
            cur.next = nextNode
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummyHead.next

def createListNode(l: List[int], cur: int) -> ListNode:
    if cur >= len(l):
        return None
    curNode = ListNode(l[cur])
    curNode.next = createListNode(l, cur + 1)
    return curNode

def createListNodes(l: List[int]) -> ListNode:
    return createListNode(l, 0)

def printAns(l: ListNode) -> None:
    while l:
        print(l.val)
        l = l.next

if __name__ == "__main__":
    l1 = createListNodes([2, 4, 3])
    l2 = createListNodes([5, 6, 4])
    s = Solution2()
    result = s.addTwoNumbers(l1, l2)
    printAns(result)