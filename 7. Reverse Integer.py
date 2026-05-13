class Solution:
    def reverse(self, x):

        # Lưu dấu âm/dương
        dau = -1 if x < 0 else 1

        # Đổi thành số dương
        x = abs(x)

        # Kết quả đảo
        dao = 0

        # Khi x còn chữ số
        while x != 0:

            # Lấy chữ số cuối
            soCuoi = x % 10

            # Thêm vào số đảo
            dao = dao * 10 + soCuoi

            # Bỏ chữ số cuối
            x = x // 10

        # Gắn lại dấu
        dao = dao * dau

        # Kiểm tra tràn số 32-bit
        if dao < -2**31 or dao > 2**31 - 1:
            return 0

        return dao