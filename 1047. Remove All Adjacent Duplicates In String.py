class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Bước 1: Khởi tạo một stack (dùng list trong Python)
        stack = []

        # Bước 2: Duyệt qua từng ký tự trong chuỗi
        for char in s:
            # Nếu stack không rỗng và ký tự hiện tại trùng với ký tự cuối cùng trong stack
            if stack and stack[-1] == char:
                stack.pop()  # loại bỏ ký tự trùng lặp (xóa cặp)
            else:
                stack.append(char)  # thêm ký tự vào stack nếu không trùng

        # Bước 3: Ghép các ký tự còn lại trong stack thành chuỗi kết quả
        return "".join(stack)