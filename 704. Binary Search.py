from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Bước 1: Khởi tạo hai con trỏ để xác định phạm vi tìm kiếm
        left = 0
        right = len(nums) - 1

        # Bước 2: Dùng vòng lặp để thu hẹp phạm vi tìm kiếm
        while left <= right:
            # Tính chỉ số giữa
            mid = (left + right) // 2

            # Nếu phần tử giữa bằng target → trả về chỉ số mid
            if nums[mid] == target:
                return mid
            # Nếu phần tử giữa nhỏ hơn target → dịch sang nửa phải
            elif nums[mid] < target:
                left = mid + 1
            # Nếu phần tử giữa lớn hơn target → dịch sang nửa trái
            else:
                right = mid - 1

        # Bước 3: Nếu không tìm thấy → trả về -1
        return -1