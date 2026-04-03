from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Không trả về gì, mà chỉnh sửa trực tiếp mảng s.
        """
        # Bước 1: Khởi tạo hai con trỏ
        left = 0               # con trỏ bắt đầu từ đầu mảng
        right = len(s) - 1     # con trỏ bắt đầu từ cuối mảng

        # Bước 2: Duyệt cho đến khi hai con trỏ gặp nhau
        while left < right:
            # Hoán đổi phần tử ở vị trí left và right
            s[left], s[right] = s[right], s[left]

            # Di chuyển con trỏ left sang phải
            left += 1
            # Di chuyển con trỏ right sang trái
            right -= 1