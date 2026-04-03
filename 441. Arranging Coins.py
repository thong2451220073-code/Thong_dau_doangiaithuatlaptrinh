class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Khởi tạo phạm vi tìm kiếm
        left, right = 0, n

        # Dùng Binary Search để tìm số hàng đầy đủ
        while left <= right:
            mid = (left + right) // 2  # lấy số giữa

            # Tính tổng số đồng cần để xếp mid hàng đầy đủ
            coins = mid * (mid + 1) // 2

            if coins == n:
                # Nếu vừa đủ → mid chính là số hàng đầy đủ
                return mid
            elif coins < n:
                # Nếu chưa đủ → có thể xếp thêm hàng → dịch sang phải
                left = mid + 1
            else:
                # Nếu vượt quá số đồng → phải giảm số hàng → dịch sang trái
                right = mid - 1

        # Khi vòng lặp kết thúc, right sẽ là số hàng đầy đủ nhất có thể
        return right