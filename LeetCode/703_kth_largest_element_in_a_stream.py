import heapq
from typing import List

class KthLargest:

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

    def add(self, val: int) -> int:
        if len(self.heapq) < self.k:
            res = heapq.heappushpop(self.heapq, val)
            heapq.heappush(self.heapq, res)
            return res
        heapq.heappushpop(self.heapq, val)
        res = heapq.heappop(self.heapq)
        heapq.heappush(self.heapq, res)
        return res
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)