class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        target = sorted(s1)

        for i in range(len(s2) - size + 1):
            window = s2[i:i + size]
            if sorted(window) == target:
                return True

        return False