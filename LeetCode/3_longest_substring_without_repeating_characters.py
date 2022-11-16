# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 8:25

# TC: O(n^2)?
# SC: O(n)?
class Solution1:
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

# TC: O(n)
# SC: O(n)
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, r = 0, 0
        res = 0
        existed = set()
        while r < len(s):
            while r < len(s) and s[r] not in existed:
                existed.add(s[r])
                r += 1
            res = max(res, r - i)
            existed.discard(s[i])
            i += 1
        return res

# TC: O(n)
# SC: O(n)
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            res = max(res, j - i + 1)
            mp[s[j]] = j + 1
        return res