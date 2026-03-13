from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()  # sắp xếp mảng
        
        result = []  # lưu các index
        
        for i in range(len(nums)):  # duyệt từng phần tử
            if nums[i] == target:   # nếu bằng target
                result.append(i)    # lưu index
        
        return result
