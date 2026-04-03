from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Nếu mảng rỗng thì không có phần tử nào
        if not nums:
            return 0

        # Khởi tạo con trỏ 'i' để đánh dấu vị trí của phần tử duy nhất cuối cùng
        i = 0  

        # Duyệt qua mảng từ phần tử thứ 2 trở đi
        for j in range(1, len(nums)):
            # Nếu nums[j] khác nums[i], tức là tìm thấy phần tử mới (không trùng lặp)
            if nums[j] != nums[i]:
                i += 1              # Tăng vị trí 'i' lên để lưu phần tử mới
                nums[i] = nums[j]  # Ghi đè phần tử mới vào vị trí i

        # Số phần tử duy nhất chính là i + 1 (vì i bắt đầu từ 0)
        return i + 1