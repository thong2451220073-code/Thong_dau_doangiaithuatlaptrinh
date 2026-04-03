from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Bước 1: Chuyển nums thành set để tìm kiếm nhanh hơn (O(1))
        num_set = set(nums)

        # Bước 2: Lặp cho đến khi original không còn trong nums
        while original in num_set:
            # Nếu tìm thấy original trong nums thì nhân đôi nó
            original *= 2

        # Bước 3: Khi không còn tìm thấy nữa thì trả về kết quả
        return original