class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        occurList = [0] * 26
        for c in s:
            occurList[ord(c) - ord('a')] += 1
        for c in t:
            occurList[ord(c) - ord('a')] -= 1
        return not any(occurList)