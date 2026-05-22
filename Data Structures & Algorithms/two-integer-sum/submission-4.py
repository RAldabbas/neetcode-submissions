class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tMap = {}
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in tMap:
                return [tMap[diff], j]
            tMap[nums[j]] = j
        


        