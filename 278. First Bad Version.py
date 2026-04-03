# Giả lập version lỗi đầu tiên
bad = 4   # giả sử version 4 trở đi bị lỗi

# Hàm kiểm tra version có lỗi hay không
def isBadVersion(version):
    return version >= bad


class Solution:
    # Định nghĩa hàm firstBadVersion với tham số n là số version
    def firstBadVersion(self, n: int) -> int:

        # left là version bắt đầu tìm (1)
        # right là version cuối cùng (n)
        left, right = 1, n

        # Lặp khi left vẫn nhỏ hơn right
        while left < right:

            # Tính version ở giữa
            mid = (left + right) // 2

            # Kiểm tra version giữa có bị lỗi không
            if isBadVersion(mid):

                # Nếu mid bị lỗi → lỗi có thể ở mid hoặc bên trái
                right = mid

            else:
                # Nếu mid không lỗi → lỗi nằm bên phải
                left = mid + 1

        # Khi vòng lặp kết thúc → left chính là version lỗi đầu tiên
        return left


# Tạo object Solution
s = Solution()

# Test thử với 5 version
print("First bad version là:", s.firstBadVersion(5))
