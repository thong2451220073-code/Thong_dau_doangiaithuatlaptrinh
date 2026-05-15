class Solution:
    def plusOne(self, digits):
        n = len(digits)

        # Duyệt từ cuối về đầu
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # Nếu toàn bộ đều là 9
        return [1] + digits
