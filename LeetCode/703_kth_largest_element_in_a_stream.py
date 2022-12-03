import heapq
from typing import List

# 28:12
# SC: O(k)
class KthLargest:

    # TC: O(nlogk)
    def __init__(self, k: int, nums: List[int]):
        self.heapq = []
        self.k = k
        heapq.heapify(self.heapq)
        for num in nums:
            if len(self.heapq) == self.k:
                minN = heapq.heappop(self.heapq)
                heapq.heappush(self.heapq, max(minN, num))
            else:
                heapq.heappush(self.heapq, num)

    # TC: O(logk)
    def add1(self, val: int) -> int:
        if len(self.heapq) < self.k:
            heapq.heappush(self.heapq, val)
        else:
            heapq.heappushpop(self.heapq, val)
        return self.heapq[0]
    
    # TC: O(logk)
    def add2(self, val: int) -> int:
        heapq.heappush(self.heapq, val)
        if len(self.heapq) > self.k:
            heapq.heappop(self.heapq)
        return self.heapq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)