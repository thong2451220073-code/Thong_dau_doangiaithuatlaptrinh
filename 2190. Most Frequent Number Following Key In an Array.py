from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        freq = {}  # dictionary để đếm số lần xuất hiện
        
        # duyệt mảng (trừ phần tử cuối)
        for i in range(len(nums) - 1):
            
            # nếu phần tử hiện tại bằng key
            if nums[i] == key:
                
                target = nums[i + 1]  # lấy số đứng sau key
                
                # cập nhật số lần xuất hiện trong dictionary
                if target in freq:
                    freq[target] += 1
                else:
                    freq[target] = 1
        
        # tìm số có tần suất lớn nhất
        max_count = 0
        result = 0
        
        for num in freq:
            if freq[num] > max_count:
                max_count = freq[num]
                result = num
        
        return result
