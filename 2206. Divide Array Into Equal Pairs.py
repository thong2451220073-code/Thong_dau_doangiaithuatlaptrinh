from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        freq = {}  # dictionary để đếm số lần xuất hiện
        
        # đếm số lần xuất hiện của mỗi số
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # kiểm tra xem có số nào xuất hiện lẻ lần không
        for count in freq.values():
            if count % 2 != 0:   # nếu là số lẻ
                return False
        
        return True
