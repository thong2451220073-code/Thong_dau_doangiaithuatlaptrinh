from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Nếu tìm thấy target → trả về ngay
            if nums[mid] == target:
                return mid

            # Xác định nửa nào đang được sắp xếp tăng dần
            if nums[left] <= nums[mid]:
                # Nửa trái được sắp xếp
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Nửa phải được sắp xếp
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Nếu không tìm thấy
        return -1