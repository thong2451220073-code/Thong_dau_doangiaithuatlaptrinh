class Solution:

    def isPowerOfTwo(self, n: int) -> bool:

        # số <= 0 chắc chắn không phải lũy thừa của 2
        if n <= 0:
            return False

        # chia liên tục cho 2
        while n % 2 == 0:

            # nếu chia hết cho 2 thì chia tiếp
            n = n // 2

        # nếu cuối cùng còn lại 1
        # thì là lũy thừa của 2
        return n == 1