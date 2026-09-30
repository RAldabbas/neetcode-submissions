class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        bestLeft = 0
        bestLength = float("inf")

        tMap = {}
        sMap = {}

        if len(s) < len(t):
            return ""

        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        have = 0
        needed = len(tMap)

        for r, c in enumerate(s):
            sMap[c] = sMap.get(c, 0) + 1

            if c in tMap and sMap[c] == tMap[c]:
                have += 1

            while have == needed:
                if (r - l + 1) < bestLength:
                    bestLength = r - l + 1
                    bestLeft = l

                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        
        if bestLength == float("inf"):
            return ""
        return s[bestLeft:bestLeft + bestLength]        