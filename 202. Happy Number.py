class Solution:
    def isHappy(self, n):

        # Lưu các số đã gặp
        daGap = set()

        # Lặp cho tới khi ra 1
        while n != 1:

            # Nếu số đã xuất hiện trước đó
            if n in daGap:

                # Đang bị lặp vô hạn
                return False

            # Thêm vào set
            daGap.add(n)

            # Tính tổng bình phương chữ số
            tong = 0

            while n > 0:

                # Lấy chữ số cuối
                soCuoi = n % 10

                # Cộng bình phương
                tong += soCuoi * soCuoi

                # Bỏ chữ số cuối
                n = n // 10

            # Cập nhật n
            n = tong

        # Nếu ra 1
        return True