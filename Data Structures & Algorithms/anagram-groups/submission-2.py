class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        anagramCheck = [0] * 26
        for str in strs:
            anagramCheckCpy = anagramCheck.copy()
            for char in str:
                anagramCheckCpy[ord(char) - ord('a')] += 1
            sortedMap.setdefault(tuple(anagramCheckCpy), []).append(str)

        return list(sortedMap.values())
