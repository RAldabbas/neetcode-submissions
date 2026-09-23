class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxSubStr = 0, 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                maxSubStr = max(maxSubStr, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])

        return max(maxSubStr, len(seen))