# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 8:25

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s) - res:
            l = self.lengthOfSubstring(s[i:])
            res = max(l, res)
            i += 1
        return res
    
    def lengthOfSubstring(self, s: str) -> int:
        existed = set()
        i = 0
        while i < len(s):
            if s[i] in existed:
                return i
            existed.add(s[i])
            i += 1
        return i