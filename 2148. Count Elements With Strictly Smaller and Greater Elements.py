class Solution:
    def countElements(self, nums):
        # Tìm giá trị nhỏ nhất và lớn nhất
        min_val = min(nums)
        max_val = max(nums)
        
        count = 0
        
        # Duyệt từng phần tử
        for x in nums:
            
            # Nếu nằm giữa (không phải min, không phải max)
            if min_val < x < max_val:
                count += 1
        
        return count
