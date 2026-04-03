# Giả sử số cần đoán là 6
pick = 6

# Tạo hàm guess giống như trên LeetCode
def guess(num):
    if num > pick:
        return -1   # đoán quá lớn
    elif num < pick:
        return 1    # đoán quá nhỏ
    else:
        return 0    # đoán đúng


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1        # điểm bắt đầu
        right = n       # điểm kết thúc

        while left <= right:   # khi khoảng vẫn còn
            mid = (left + right) // 2   # lấy số ở giữa

            result = guess(mid)   # kiểm tra số mid

            if result == 0:
                return mid        # nếu đúng → trả về mid

            elif result == -1:
                right = mid - 1   # nếu mid quá lớn → tìm bên trái

            else:
                left = mid + 1    # nếu mid quá nhỏ → tìm bên phải


# chạy thử chương trình
n = 10
s = Solution()

print("Số cần tìm là:", s.guessNumber(n))
