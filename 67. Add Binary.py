class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # i trỏ cuối chuỗi a
        i = len(a) - 1

        # j trỏ cuối chuỗi b
        j = len(b) - 1

        # biến nhớ
        nho = 0

        # lưu kết quả
        kq = []

        # lặp khi còn phần tử hoặc còn nhớ
        while i >= 0 or j >= 0 or nho:

            # tổng ban đầu bằng số nhớ
            tong = nho

            # nếu a còn phần tử
            if i >= 0:
                tong += int(a[i])
                i -= 1

            # nếu b còn phần tử
            if j >= 0:
                tong += int(b[j])
                j -= 1

            # lấy bit kết quả
            kq.append(str(tong % 2))

            # cập nhật số nhớ
            nho = tong // 2

        # đảo ngược rồi nối thành chuỗi
        return ''.join(reversed(kq))