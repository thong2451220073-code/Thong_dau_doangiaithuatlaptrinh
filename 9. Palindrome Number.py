class Solution:
    def isPalindrome(self, x):

        # Số âm chắc chắn không phải palindrome
        if x < 0:
            return False

        # Lưu số ban đầu
        original = x

        # Số đảo
        reverse = 0

        # Đảo số
        while x > 0:

            # Lấy chữ số cuối
            digit = x % 10

            # Thêm vào số đảo
            reverse = reverse * 10 + digit

            # Bỏ chữ số cuối
            x = x // 10

        # So sánh
        return original == reverse