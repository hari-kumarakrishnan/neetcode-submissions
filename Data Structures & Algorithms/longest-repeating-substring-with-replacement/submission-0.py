class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        startWindow, endWindow = 0, 0
        maxFreq = 0
        res = 0
        while endWindow < len(s):
            freq[s[endWindow]] = 1 + freq.get(s[endWindow], 0)
            maxFreq = max(maxFreq, freq[s[endWindow]])
            while (endWindow - startWindow + 1) - maxFreq > k:
                freq[s[startWindow]] -= 1
                startWindow += 1
            res = max(res, endWindow - startWindow + 1)
            endWindow += 1
        return res
