class Solution:

    def addDigits(self, num: int) -> int:

        # lặp cho tới khi num chỉ còn 1 chữ số
        while num >= 10:

            # lưu tổng các chữ số
            tong = 0

            # tách từng chữ số ra để cộng
            while num > 0:

                # lấy chữ số cuối
                tong += num % 10

                # bỏ chữ số cuối
                num = num // 10

            # cập nhật num bằng tổng mới
            num = tong

        # trả về kết quả cuối cùng
        return num