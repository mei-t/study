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
class MinStack1:

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
#   TC:O(1)
# stackに何もない場合のtop()、getMin()の挙動は定義されていない。
class MinStack2:

    def __init__(self):
        self.stack = deque()
        

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            minVal = min(val, self.stack[-1][1])
        else:
            minVal = val
        self.stack.append([val, minVal])
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


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
#   TC:O(1)
# stackに何もない場合のtop()、getMin()の挙動は定義されていない。
class MinStack3:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack[-1] == val:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


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
#   TC:O(1)
# stackに何もない場合のtop()、getMin()の挙動は定義されていない。
class MinStack4:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val < self.minStack[-1][0]:
            self.minStack.append([val,1])
        elif val == self.minStack[-1][0]:
            self.minStack[-1][1] += 1
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
        if self.minStack[-1][1] == 0:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1][0]
        