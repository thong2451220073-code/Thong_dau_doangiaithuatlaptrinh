class Solution:
    def missingNumber(self, nums):

        # Số phần tử
        n = len(nums)

        # Tổng đầy đủ từ 0 -> n
        tongDayDu = n * (n + 1) // 2

        # Tổng trong mảng
        tongMang = sum(nums)

        # Số bị thiếu
        return tongDayDu - tongMang