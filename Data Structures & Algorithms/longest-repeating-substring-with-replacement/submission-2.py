class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ret = 0
        occurMap = {}
        maxFreq = 0

        for i, r in enumerate(s):
            occurMap[r] = occurMap.get(r, 0) + 1
            maxFreq = max(maxFreq, occurMap[r])
            reqReplacements = (i - l + 1) - maxFreq
            
            if (reqReplacements > k):
                occurMap[s[l]] -= 1
                l += 1
                
            ret = max(ret, i - l + 1)

        return ret


        
            