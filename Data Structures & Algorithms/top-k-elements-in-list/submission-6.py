class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        occurMap = defaultdict(int)
        for num in nums:
            occurMap[num] += 1
        
        for num, count in occurMap.items():
            freqList[count].append(num)
        retList = []

        for i in range(len(freqList) - 1, -1, -1):
            if not len(freqList[i]):
                continue
            
            for el in freqList[i]:
                if k == 0:
                    return retList
                retList.append(el)
                k -= 1


        return retList