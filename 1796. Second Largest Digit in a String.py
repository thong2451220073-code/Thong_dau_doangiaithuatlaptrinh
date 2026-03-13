class Solution:
    def secondHighest(self, s: str) -> int:
        
        digits = set()   # lưu các số khác nhau
        
        # duyệt từng ký tự trong chuỗi
        for c in s:
            if c.isdigit():        # kiểm tra có phải số không
                digits.add(int(c)) # thêm vào set
        
        # nếu có ít hơn 2 số
        if len(digits) < 2:
            return -1
        
        # sắp xếp giảm dần
        digits = sorted(digits, reverse=True)
        
        # trả về số lớn thứ 2
        return digits[1]
