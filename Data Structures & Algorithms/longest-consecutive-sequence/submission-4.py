class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_c = 0
        for i in s:
            if i - 1 in s:
                continue
            temp = 1
            while (i + 1) in s:
                i += 1
                temp += 1
            max_c = max(temp, max_c)
        return max_c
