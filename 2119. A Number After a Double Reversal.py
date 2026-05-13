class Solution:
    def isSameAfterReversals(self, num):

        # Nếu num = 0
        # hoặc không kết thúc bằng 0
        if num == 0 or num % 10 != 0:
            return True

        # Nếu kết thúc bằng 0
        return False