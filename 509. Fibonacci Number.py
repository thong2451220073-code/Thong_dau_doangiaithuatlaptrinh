class Solution:
    def fib(self, n):

        # Trường hợp đặc biệt
        if n == 0:
            return 0

        if n == 1:
            return 1

        # Hai số đầu tiên
        a = 0
        b = 1

        # Tính từ F(2) tới F(n)
        for i in range(2, n + 1):

            # Số Fibonacci mới
            c = a + b

            # Dời sang phải
            a = b
            b = c

        # Kết quả cuối
        return b