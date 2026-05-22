class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums).most_common(k)
        res = []
        for el in cnt:
            res.append(el[0])
        return res
        