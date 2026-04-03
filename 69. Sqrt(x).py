class Solution:
    def mySqrt(self, x: int) -> int:
        # Nếu x < 2 thì căn bậc hai nguyên chính là x (0 hoặc 1)
        if x < 2:
            return x

        # Khởi tạo phạm vi tìm kiếm từ 2 đến x//2
        # Vì căn bậc hai của x luôn nhỏ hơn hoặc bằng x//2 khi x >= 2
        left, right = 2, x // 2

        # Dùng Binary Search để thu hẹp phạm vi
        while left <= right:
            mid = (left + right) // 2  # lấy số giữa
            sq = mid * mid             # bình phương số giữa

            if sq == x:
                # Nếu bình phương bằng x → trả về mid
                return mid
            elif sq < x:
                # Nếu bình phương nhỏ hơn x → dịch sang phải
                left = mid + 1
            else:
                # Nếu bình phương lớn hơn x → dịch sang trái
                right = mid - 1

        # Khi vòng lặp kết thúc, right sẽ là căn bậc hai nguyên của x
        return right