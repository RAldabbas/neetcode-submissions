class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        anagramCheck = [0] * 26
        for s in strs:
            anagramCheckCpy = anagramCheck.copy()
            for c in s:
                anagramCheckCpy[ord(c) - ord('a')] += 1
            sortedMap.setdefault(tuple(anagramCheckCpy), []).append(s)

        return list(sortedMap.values())
