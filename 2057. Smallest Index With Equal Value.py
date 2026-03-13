from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        # duyệt qua từng index
        for i in range(len(nums)):
            
            # kiểm tra điều kiện
            if i % 10 == nums[i]:
                return i
        
        # nếu không tìm thấy
        return -1
