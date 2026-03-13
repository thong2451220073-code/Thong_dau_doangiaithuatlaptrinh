from typing import List   # khai báo kiểu dữ liệu List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)   # số lượng nhà
        
        max_dist = 0      # lưu khoảng cách lớn nhất
        
        # so sánh nhà đầu tiên với các nhà phía sau
        for i in range(n):
            if colors[i] != colors[0]:          # nếu màu khác
                max_dist = max(max_dist, i)     # khoảng cách = i - 0
        
        # so sánh nhà cuối với các nhà phía trước
        for i in range(n):
            if colors[i] != colors[n-1]:        # nếu màu khác
                max_dist = max(max_dist, n-1-i) # khoảng cách
        
        return max_dist
