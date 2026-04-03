from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Không trả về gì, mà chỉnh sửa trực tiếp mảng nums1.
        """
        # Bước 1: Khởi tạo 3 con trỏ
        i = m - 1          # con trỏ cuối cùng của phần tử hợp lệ trong nums1
        j = n - 1          # con trỏ cuối cùng của nums2
        k = m + n - 1      # con trỏ cuối cùng của nums1 (bao gồm chỗ trống)

        # Bước 2: Duyệt từ cuối mảng về đầu
        while i >= 0 and j >= 0:
            # So sánh phần tử cuối cùng của nums1 và nums2
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # đặt phần tử lớn hơn vào cuối nums1
                i -= 1               # lùi con trỏ i
            else:
                nums1[k] = nums2[j]  # đặt phần tử lớn hơn vào cuối nums1
                j -= 1               # lùi con trỏ j
            k -= 1                   # lùi con trỏ k

        # Bước 3: Nếu còn phần tử trong nums2 thì chép nốt vào nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1