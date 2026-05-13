class Solution:
    def majorityElement(self, nums):

        # Ứng viên majority
        candidate = 0

        # Số phiếu
        count = 0

        # Duyệt mảng
        for num in nums:

            # Nếu hết phiếu
            if count == 0:

                # Chọn ứng viên mới
                candidate = num

            # Nếu giống ứng viên
            if num == candidate:

                # Tăng phiếu
                count += 1

            else:
                # Khác ứng viên
                # Giảm phiếu
                count -= 1

        # Candidate cuối cùng là majority
        return candidate