from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Bước 1: Khởi tạo phạm vi tìm kiếm
        left = 0
        right = len(nums) - 1

        # Bước 2: Dùng Binary Search để tìm vị trí
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # Nếu tìm thấy target → trả về chỉ số mid
                return mid
            elif nums[mid] < target:
                # Nếu nums[mid] < target → dịch sang nửa phải
                left = mid + 1
            else:
                # Nếu nums[mid] > target → dịch sang nửa trái
                right = mid - 1

        # Bước 3: Nếu không tìm thấy target → vị trí chèn sẽ là left
        return left