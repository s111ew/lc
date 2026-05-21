class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        curr_max = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] > nums[j-1]:
                while j < len(nums) and nums[j] > nums[j-1]:
                    j+=1
                curr_max = max(curr_max, j - i)
            elif nums[j] < nums[j-1]:
                while j < len(nums) and nums[j] < nums[j-1]:
                    j+=1
                curr_max = max(curr_max, j - i)
            else:
                while j < len(nums) and nums[j] == nums[j-1]:
                    j+=1
            i = j-1
        return curr_max