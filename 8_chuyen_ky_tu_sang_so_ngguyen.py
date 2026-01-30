class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. Bỏ khoảng trắng đầu
        while i < n and s[i] == ' ':
            i += 1

        # 2. Kiểm tra dấu
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Đọc các chữ số
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # 4. Giới hạn 32-bit
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))              # 42
    print(sol.myAtoi("   -42"))          # -42
    print(sol.myAtoi("4193 with words")) # 4193
    print(sol.myAtoi("words 4193"))      # 0