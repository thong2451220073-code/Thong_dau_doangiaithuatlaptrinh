from typing import List
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        # Đếm số lần xuất hiện của từng ký tự trong chuỗi
        count = Counter(s)

        # Lấy danh sách các số lần xuất hiện
        values = list(count.values())

        # Lấy số lần xuất hiện của ký tự đầu tiên để làm chuẩn so sánh
        first = values[0]

        # Duyệt qua từng số lần xuất hiện
        for v in values:

            # Nếu có ký tự nào khác số lần xuất hiện
            if v != first:
                return False

        # Nếu tất cả đều giống nhau
        return True
