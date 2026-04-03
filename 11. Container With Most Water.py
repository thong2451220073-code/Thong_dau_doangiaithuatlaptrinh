from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Khởi tạo hai con trỏ: left ở đầu, right ở cuối mảng
        left = 0
        right = len(height) - 1
        
        # Biến max_area để lưu diện tích lớn nhất tìm được
        max_area = 0
        
        # Lặp cho đến khi hai con trỏ gặp nhau
        while left < right:
            # Chiều cao giới hạn bởi thanh nhỏ hơn trong hai thanh hiện tại
            current_height = min(height[left], height[right])
            # Chiều rộng là khoảng cách giữa hai con trỏ
            width = right - left
            # Diện tích hiện tại
            area = current_height * width
            # Cập nhật diện tích lớn nhất nếu cần
            max_area = max(max_area, area)
            
            # Dịch chuyển con trỏ của thanh nhỏ hơn
            if height[left] < height[right]:
                left += 1  # Tăng left nếu thanh bên trái nhỏ hơn
            else:
                right -= 1  # Giảm right nếu thanh bên phải nhỏ hơn hoặc bằng
            
        return max_area  # Trả về diện tích lớn nhất