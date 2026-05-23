class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)   
        post_fix = 1

        for i, num in enumerate(nums):
            if i == 0:
                res[i] = num
            else:
                res[i] = res[i - 1] * num
        print(res)
        for j in range(len(nums) - 1, -1, -1):
            if j == 0:
                res[j] = post_fix
            else:
                res[j] = res[j - 1] * post_fix
                post_fix *= nums[j]
        print(res)
        return res
        
        
