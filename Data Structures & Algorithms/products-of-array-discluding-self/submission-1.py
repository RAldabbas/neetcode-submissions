class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        numZeros = 0
        retList = []
        for num in nums:
            if num:
                totalProduct *= num
            else:
                numZeros += 1
        
        if numZeros > 1:
            return [0] * len(nums)

        for num in nums:
            if numZeros:
                if num:
                    retList.append(0)
                else:
                    retList.append(totalProduct)
            else:
                retList.append(totalProduct // num)
        return retList