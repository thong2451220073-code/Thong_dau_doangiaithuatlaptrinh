class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Chuyển về chữ thường và lọc ký tự chữ + số
        filtered = ""
        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()

        # So sánh với chuỗi đảo ngược
        return filtered == filtered[::-1]