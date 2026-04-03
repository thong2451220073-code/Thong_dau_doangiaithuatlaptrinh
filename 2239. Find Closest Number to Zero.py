# Bài 2239: Find Closest Number to Zero

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # Khởi tạo biến lưu kết quả, giả sử phần tử đầu tiên là gần 0 nhất
        closest = nums[0]

        # Duyệt từng phần tử trong mảng
        for num in nums:
            # So sánh khoảng cách tới 0 bằng giá trị tuyệt đối
            # Nếu num gần 0 hơn closest
            if abs(num) < abs(closest):
                closest = num
            # Nếu khoảng cách bằng nhau thì chọn số lớn hơn
            elif abs(num) == abs(closest) and num > closest:
                closest = num

        # Trả về số gần 0 nhất
        return closest