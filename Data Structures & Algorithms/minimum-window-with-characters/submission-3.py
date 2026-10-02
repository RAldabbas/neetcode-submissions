class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # idea is: keep track of num chars have so far and num chars needed to still get
        if len(s) < len(t):
            return ""
        
        target = {}
        window = {}
        for i in range(len(t)):
            target[t[i]] = target.get(t[i], 0) + 1
        print(target)

        have = 0
        needed = len(target)
        l = 0
        bestL = 0
        bestSoFar = float("inf")

        # loop till all chars are in window, update best val and while loop to shorten window from left till invalid
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in target and window[c] == target[c]:
                have += 1
            
            while have == needed:
                windowSize = r - l + 1
                if windowSize < bestSoFar:
                    bestSoFar = windowSize
                    bestL = l
                
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        
        if bestSoFar == float("inf"):
            return ""
        
        return s[bestL:bestL + bestSoFar]
            
        


        
