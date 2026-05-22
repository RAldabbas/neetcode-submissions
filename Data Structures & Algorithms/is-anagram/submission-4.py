class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        occurList = [0] * 26
        for i in range(len(s)):
            occurList[ord(s[i]) - ord('a')] += 1
            occurList[ord(t[i]) - ord('a')] -= 1
        return not any(occurList)