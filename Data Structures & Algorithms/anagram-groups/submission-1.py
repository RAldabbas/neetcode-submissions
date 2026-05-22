class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            sortedMap.setdefault(sortedStr, []).append(str)
        return list(sortedMap.values())
