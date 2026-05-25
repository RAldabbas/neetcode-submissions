class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)  
        pre_fix = 1 
        post_fix = 1

        for i in range(len(nums)):
            res[i] = pre_fix
            pre_fix = pre_fix * nums[i]

        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * post_fix
            post_fix = post_fix * nums[j]
        return res
        
        
