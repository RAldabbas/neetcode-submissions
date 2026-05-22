class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        for s in strs:
            anagramCheck = [0] * 26
            for c in s:
                anagramCheck[ord(c) - ord('a')] += 1
            sortedMap.setdefault(tuple(anagramCheck), []).append(s)

        return list(sortedMap.values())
