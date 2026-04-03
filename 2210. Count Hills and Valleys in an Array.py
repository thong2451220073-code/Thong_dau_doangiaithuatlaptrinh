from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        arr = [nums[0]]  # mảng mới để loại bỏ số trùng
        
        # bỏ các số trùng liên tiếp
        for num in nums[1:]:
            if num != arr[-1]:
                arr.append(num)
        
        count = 0
        
        # duyệt từ phần tử thứ 2 đến gần cuối
        for i in range(1, len(arr) - 1):
            
            # kiểm tra hill
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                count += 1
            
            # kiểm tra valley
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                count += 1
        
        return count
