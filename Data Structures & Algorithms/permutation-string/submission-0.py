class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
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

        print("checker:", freqMap1)
        for i in range(r + 1, len(s2)):  
            freqMap2[ord(s2[l]) - ord('a')] -= 1
            freqMap2[ord(s2[i]) - ord('a')] += 1
            print(freqMap2)
            if (freqMap1 == freqMap2):
                return True
            l += 1
        return freqMap1 == freqMap2




        
        
            

            