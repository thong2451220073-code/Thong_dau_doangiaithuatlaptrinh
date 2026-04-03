class Solution:
    def isValid(self, s: str) -> bool:
        # Bước 1: Khởi tạo stack để lưu các dấu mở ngoặc
        stack = []
        
        # Bước 2: Tạo một dictionary để ánh xạ dấu đóng → dấu mở tương ứng
        mapping = {")": "(", "}": "{", "]": "["}
        
        # Bước 3: Duyệt qua từng ký tự trong chuỗi
        for char in s:
            # Nếu là dấu đóng ngoặc
            if char in mapping:
                # Lấy phần tử cuối cùng trong stack (nếu có), nếu stack rỗng thì gán giá trị giả '#'
                top_element = stack.pop() if stack else "#"
                
                # Kiểm tra xem có khớp với dấu mở tương ứng không
                if mapping[char] != top_element:
                    return False
            else:
                # Nếu là dấu mở ngoặc thì thêm vào stack
                stack.append(char)
        
        # Bước 4: Nếu stack rỗng sau khi duyệt hết → hợp lệ
        return not stack