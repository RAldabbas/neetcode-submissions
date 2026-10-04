class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle
        if target == nums[l]:
            return l
        
        if target >= nums[l] and target <= nums[len(nums) - 1]:
            r = len(nums) - 1
        else:
            r = l
            l = 0
        while l <= r:
            middle = (l + r) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle + 1
            else:
                r = middle - 1
        print(l, r)
        return -1
                
