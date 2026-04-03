from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Tạo một tập hợp để lưu các phần tử đã duyệt
        seen = set()

        # Duyệt qua từng phần tử trong mảng
        for num in arr:
            # Nếu đã thấy num*2 trong tập hợp → tồn tại cặp (num, num*2)
            # Hoặc nếu đã thấy num/2 (và num chẵn) → tồn tại cặp (num/2, num)
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True

            # Thêm phần tử hiện tại vào tập hợp để kiểm tra cho các phần tử sau
            seen.add(num)

        # Nếu duyệt hết mà không tìm thấy cặp nào → trả về False
        return False