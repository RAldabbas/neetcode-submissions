class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen = 0, 0
        seenMap = {}
        for i, c in enumerate(s):
            if c in seenMap and seenMap[c] >= l:
                l = seenMap[c] + 1
            seenMap[c] = i
            maxLen = max(maxLen, i - l + 1)

        return maxLen