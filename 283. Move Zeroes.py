from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Không trả về gì, mà chỉnh sửa trực tiếp mảng nums.
        """
        # Bước 1: Khởi tạo con trỏ index để ghi đè các phần tử khác 0
        index = 0

        # Bước 2: Duyệt qua từng phần tử trong mảng
        for i in range(len(nums)):
            # Nếu phần tử khác 0 thì đưa nó về vị trí index
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        # Bước 3: Sau khi đã đưa hết phần tử khác 0 về đầu mảng,
        # điền các số 0 vào phần còn lại
        while index < len(nums):
            nums[index] = 0
            index += 1