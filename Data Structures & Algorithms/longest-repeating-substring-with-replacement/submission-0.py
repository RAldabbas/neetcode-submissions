class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ret = 0
        occurMap = {}

        for i, r in enumerate(s):
            occurMap[r] = occurMap.get(r, 0) + 1
            maxFreq = max(occurMap.values())
            reqReplacements = (i - l + 1) - maxFreq
            
            while (reqReplacements > k):
                occurMap[s[l]] -= 1
                l += 1
                maxFreq = max(occurMap.values())
                reqReplacements = (i - l + 1) - maxFreq


            ret = max(ret, maxFreq + reqReplacements)


            
        
        return ret


        
            