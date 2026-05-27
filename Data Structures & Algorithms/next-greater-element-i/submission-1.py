class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        to_check = {}
        for n in nums1:
            to_check[n] = 0
        stack = []
        out = []
        for i in range(len(nums2)-1, -1, -1):
            to_push = -1
            if len(stack) == 0:
                stack.append(nums2[i])
            if len(stack) > 0 and stack[-1] < nums2[i]:
                while len(stack) > 0 and stack[-1] < nums2[i]:
                    stack.pop()
                if len(stack) == 0:
                    to_push = -1
                else:
                    to_push = stack[-1]
                stack.append(nums2[i])
            elif len(stack) > 0 and stack[-1] > nums2[i]:
                to_push = stack[-1]
                stack.append(nums2[i])
            if nums2[i] in to_check:
                to_check[nums2[i]] = to_push
        for n in nums1:
            out.append(to_check[n])
        return out
                
                    
                