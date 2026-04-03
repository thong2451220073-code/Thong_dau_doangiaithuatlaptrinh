# Bài 2974: Minimum Number Game 
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        # Sắp xếp mảng tăng dần
        nums.sort()

        # Tạo mảng kết quả
        result = []

        # Duyệt từng cặp 2 phần tử
        for i in range(0, len(nums), 2):
            # Alice lấy số nhỏ hơn (nums[i])
            # Bob lấy số tiếp theo (nums[i+1])

            # Theo đề: Bob thêm trước, rồi Alice thêm
            result.append(nums[i + 1])  # Bob
            result.append(nums[i])      # Alice

        # Trả về kết quả
        return result