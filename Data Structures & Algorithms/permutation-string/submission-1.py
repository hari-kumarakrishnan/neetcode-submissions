class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1

        startWindow, endWindow = 0, 0
        current = {}

        while endWindow < len(s2):
            entering = s2[endWindow]
            current[entering] = current.get(entering, 0) + 1
            endWindow += 1

            if endWindow - startWindow > len(s1):
                leaving = s2[startWindow]
                current[leaving] -= 1
                if current[leaving] == 0:
                    del current[leaving]
                startWindow += 1

            if current == target:
                return True

        return False