from typing import List

# 3:31
# TC: O(n)
# SC: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i