class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Dictionary đếm số lần xuất hiện của mỗi ký tự
        count = {}

        # Con trỏ trái của cửa sổ
        left = 0

        # Số lần xuất hiện lớn nhất của 1 ký tự trong cửa sổ
        max_count = 0

        # Kết quả (độ dài lớn nhất)
        result = 0

        # Duyệt cửa sổ bằng con trỏ phải
        for right in range(len(s)):

            # Tăng số lần xuất hiện của ký tự hiện tại
            count[s[right]] = count.get(s[right], 0) + 1

            # Cập nhật số ký tự xuất hiện nhiều nhất
            max_count = max(max_count, count[s[right]])

            # Nếu cần đổi nhiều hơn k ký tự
            if (right - left + 1) - max_count > k:

                # Giảm số lần xuất hiện của ký tự bên trái
                count[s[left]] -= 1

                # Thu nhỏ cửa sổ
                left += 1

            # Cập nhật kết quả
            result = max(result, right - left + 1)

        return result
