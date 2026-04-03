# Bài 2558: Take Gifts From the Richest Pile 
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Lặp k lần
        for _ in range(k):
            # Tìm phần tử lớn nhất trong mảng
            max_value = max(gifts)

            # Lấy vị trí của phần tử lớn nhất
            index = gifts.index(max_value)

            # Thay bằng floor(sqrt(max_value))
            gifts[index] = int(math.sqrt(max_value))

        # Tính tổng các phần tử còn lại
        return sum(gifts)