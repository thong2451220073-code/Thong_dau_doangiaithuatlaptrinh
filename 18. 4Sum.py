from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Bước 1: Sắp xếp mảng để dễ dùng kỹ thuật hai con trỏ
        nums.sort()
        res = []
        n = len(nums)

        # Bước 2: Duyệt phần tử đầu tiên (i)
        for i in range(n - 3):
            # Tránh trùng lặp cho i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Bước 3: Duyệt phần tử thứ hai (j)
            for j in range(i + 1, n - 2):
                # Tránh trùng lặp cho j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Bước 4: Khởi tạo hai con trỏ left và right
                left = j + 1
                right = n - 1

                # Bước 5: Dùng kỹ thuật hai con trỏ để tìm cặp còn lại
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Tránh trùng lặp cho left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Tránh trùng lặp cho right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Di chuyển cả hai con trỏ
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1  # tăng tổng bằng cách dịch con trỏ trái sang phải
                    else:
                        right -= 1 # giảm tổng bằng cách dịch con trỏ phải sang trái

        return res