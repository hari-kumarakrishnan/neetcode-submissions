class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif  s > target:
                    r -= 1
                else:
                    ans.append([nums[r], nums[l], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans