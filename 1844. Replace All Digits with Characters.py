class Solution:
    def replaceDigits(self, s: str) -> str:
        
        s = list(s)  # đổi string thành list để dễ sửa
        
        # duyệt các vị trí lẻ
        for i in range(1, len(s), 2):
            
            # ký tự trước đó
            c = s[i-1]
            
            # số cần dịch
            x = int(s[i])
            
            # chuyển sang ký tự mới
            s[i] = chr(ord(c) + x)
        
        # ghép lại thành chuỗi
        return "".join(s)
