from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # Dùng Binary Search để tìm phần tử nhỏ nhất
        while left < right:
            mid = (left + right) // 2

            # Nếu nums[mid] > nums[right] → phần tử nhỏ nhất nằm bên phải
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Ngược lại, phần tử nhỏ nhất nằm bên trái (bao gồm mid)
                right = mid

        # Khi left == right → đó chính là phần tử nhỏ nhất
        return nums[left]