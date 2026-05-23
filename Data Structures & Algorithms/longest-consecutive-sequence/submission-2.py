class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            temp_longest = 1
            temp_num = num
            if num - 1 in numset:
                continue
            while temp_num + 1 in numset:
                temp_longest += 1
                temp_num += 1
            if temp_longest > longest:
                longest = temp_longest

        return longest