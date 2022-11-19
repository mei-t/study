from collections import Counter, deque
import heapq

# SC: O(n)
# __init__()
#   TC:O(1)
# push()
#   TC:O(1)
# pop()
#   TC:O(1)
# top()
#   TC:O(1)
# getMin()
#   TC:O(1) ave
#      O(n) worst
class MinStack:

    def __init__(self):
        self.stack = deque()
        minStack = []
        heapq.heapify(minStack)
        self.minStack = minStack
        self.counter = Counter(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minStack, val)
        self.counter[val] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        self.counter[val] -= 1
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        val = self.minStack[0]
        while self.counter[val] == 0:
            heapq.heappop(self.minStack)
            val = self.minStack[0]
        return val