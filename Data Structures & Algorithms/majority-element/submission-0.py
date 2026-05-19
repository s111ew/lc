class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = math.ceil(len(nums)/2)
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
            if seen[n] >= target:
                return n