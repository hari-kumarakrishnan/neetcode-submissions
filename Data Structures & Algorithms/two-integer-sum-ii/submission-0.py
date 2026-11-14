class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        s = {}

        for i in range(len(numbers)):
            if numbers[i] in s:
                return [s[numbers[i]] + 1, i + 1]
            s[target-numbers[i]] = i
        return []