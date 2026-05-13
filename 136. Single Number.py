class Solution:
    def singleNumber(self, nums):

        # Biến lưu kết quả
        ketQua = 0

        # Duyệt từng số
        for num in nums:

            # XOR với kết quả hiện tại
            ketQua ^= num

        # Số còn lại chính là đáp án
        return ketQua