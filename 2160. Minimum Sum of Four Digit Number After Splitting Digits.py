class Solution:
    def minimumSum(self, num: int) -> int:
        # Bước 1: Tách các chữ số của num thành list
        digits = [int(d) for d in str(num)]
        
        # Bước 2: Sắp xếp tăng dần
        digits.sort()
        
        # Ví dụ: num = 2932 → digits = [2,2,3,9]
        
        # Bước 3: Tạo 2 số để tổng nhỏ nhất
        # Số thứ nhất: digits[0] (nhỏ nhất) + digits[2]
        new1 = digits[0] * 10 + digits[2]
        
        # Số thứ hai: digits[1] + digits[3] (lớn nhất)
        new2 = digits[1] * 10 + digits[3]
        
        # Bước 4: Trả về tổng
        return new1 + new2