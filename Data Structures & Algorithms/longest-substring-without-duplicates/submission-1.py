class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mapper = {}
        maxValue = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in mapper and mapper[s[r]] >= l:
                l = mapper[s[r]] + 1
            mapper[s[r]] = r
            maxValue = max(maxValue, r - l + 1)
            r += 1
        return maxValue

