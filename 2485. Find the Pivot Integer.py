class Solution:
    def pivotInteger(self, n: int) -> int:
        # Tính tổng từ 1 đến n bằng công thức Gauss
        total = n * (n + 1) // 2

        # Duyệt qua từng số x từ 1 đến n
        for x in range(1, n + 1):
            # Tính tổng từ 1 đến x
            left_sum = x * (x + 1) // 2

            # Tính tổng từ x đến n = tổng toàn bộ - tổng từ 1 đến (x-1)
            right_sum = total - (x - 1) * x // 2

            # Nếu hai tổng bằng nhau → tìm thấy pivot
            if left_sum == right_sum:
                return x

        # Nếu không tìm thấy pivot → trả về -1
        return -1