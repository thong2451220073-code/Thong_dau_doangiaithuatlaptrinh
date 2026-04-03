from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Bước 1: Khởi tạo hai con trỏ
        left = 0                  # con trỏ bắt đầu từ đầu mảng
        right = len(numbers) - 1  # con trỏ bắt đầu từ cuối mảng

        # Bước 2: Duyệt cho đến khi tìm được cặp số
        while left < right:
            current_sum = numbers[left] + numbers[right]

            # Nếu tổng bằng target → trả về kết quả (chú ý mảng 1-indexed)
            if current_sum == target:
                return [left + 1, right + 1]
            
            # Nếu tổng nhỏ hơn target → tăng con trỏ trái để tăng tổng
            elif current_sum < target:
                left += 1
            
            # Nếu tổng lớn hơn target → giảm con trỏ phải để giảm tổng
            else:
                right -= 1