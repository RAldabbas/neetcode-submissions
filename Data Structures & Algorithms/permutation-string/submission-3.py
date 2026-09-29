class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1) - 1
        freqMap1 = [0] * 26
        freqMap2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            freqMap1[ord(s1[i]) - ord('a')] += 1
            freqMap2[ord(s2[i]) - ord('a')] += 1
            
        if freqMap1 == freqMap2:
            return True

        for i in range(len(s1), len(s2)):  
            freqMap2[ord(s2[i]) - ord('a')] += 1
            freqMap2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if (freqMap1 == freqMap2):
                return True
        return freqMap1 == freqMap2




        
        
            

            