class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        intSet = set(nums)
        return len(intSet) != len(nums)
        