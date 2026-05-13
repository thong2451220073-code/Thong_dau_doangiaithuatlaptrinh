class Solution:
    def decrypt(self, code, k):

        # Độ dài mảng
        n = len(code)

        # Mảng kết quả
        result = [0] * n

        # Nếu k = 0
        if k == 0:
            return result

        # Duyệt từng vị trí
        for i in range(n):

            tong = 0

            # Nếu k > 0
            if k > 0:

                # Lấy k số phía sau
                for j in range(1, k + 1):

                    # Dùng modulo để quay vòng
                    tong += code[(i + j) % n]

            else:
                # Nếu k < 0

                # Lấy |k| số phía trước
                for j in range(1, abs(k) + 1):

                    # Dùng modulo để quay vòng
                    tong += code[(i - j) % n]

            # Gán kết quả
            result[i] = tong

        return result