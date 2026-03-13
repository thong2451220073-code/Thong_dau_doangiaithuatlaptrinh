from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        count = defaultdict(int)
        
        # tính tổng nums1 + nums2
        for a in nums1:
            for b in nums2:
                count[a + b] += 1
        
        result = 0
        
        # kiểm tra nums3 + nums4
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count:
                    result += count[target]
        
        return result
