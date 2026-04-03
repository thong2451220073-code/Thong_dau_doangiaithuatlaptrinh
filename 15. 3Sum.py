class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sắp xếp mảng để dễ xử lý và dùng 2 con trỏ
        nums.sort()
        
        # Danh sách lưu kết quả
        result = []

        # Duyệt từng phần tử trong mảng
        for i in range(len(nums)):
            # Nếu phần tử hiện tại giống phần tử trước thì bỏ qua để tránh trùng
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Con trỏ trái bắt đầu sau i
            left = i + 1
            # Con trỏ phải ở cuối mảng
            right = len(nums) - 1

            # Khi 2 con trỏ chưa gặp nhau
            while left < right:
                # Tính tổng 3 số
                total = nums[i] + nums[left] + nums[right]

                # Nếu tổng bằng 0 → thỏa điều kiện
                if total == 0:
                    # Thêm bộ 3 vào kết quả
                    result.append([nums[i], nums[left], nums[right]])

                    # Di chuyển cả 2 con trỏ
                    left += 1
                    right -= 1

                    # Bỏ qua các phần tử trùng bên trái
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Bỏ qua các phần tử trùng bên phải
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Nếu tổng nhỏ hơn 0 → cần tăng tổng → dịch trái sang phải
                elif total < 0:
                    left += 1
                # Nếu tổng lớn hơn 0 → cần giảm tổng → dịch phải sang trái
                else:
                    right -= 1

        # Trả về kết quả cuối cùng
        return result