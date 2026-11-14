class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums)):
            target = -nums[i]
            mapper = {}

            for j in range(i + 1, len(nums)):
                if target - nums[j] in mapper:
                    triplet = tuple(sorted([
                        nums[i],
                        nums[j],
                        nums[mapper[target - nums[j]]]
                    ]))
                    ans.add(triplet)

                mapper[nums[j]] = j

        return [list(x) for x in ans]