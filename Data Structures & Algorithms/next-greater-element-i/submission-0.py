class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs = {}
        for i in range(len(nums2)):
            idxs[nums2[i]] = i
        
        out = []
        for n in nums1:
            i = idxs[n]
            seen_larger = False
            for j in range(i, len(nums2)):
                if nums2[j] > n:
                    out.append(nums2[j])
                    seen_larger = True
                    break
            if not seen_larger:
                out.append(-1)
        return out
                
                    
                