class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left_side = [0] * len(nums)
        right_side = [0] * len(nums)
        
        for i, num in enumerate(nums):
            if i == 0:
                left_side[i] = num
            else:
                left_side[i] = left_side[i - 1] * num
        
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right_side[j] = nums[j]
            else:
                right_side[j] = right_side[j + 1] * nums[j]
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = right_side[i + 1]
            elif i == len(nums) - 1:
                res[i] = left_side[i - 1]
            else:
                res[i] = left_side[i - 1] * right_side[i + 1]
        return res
        
        
