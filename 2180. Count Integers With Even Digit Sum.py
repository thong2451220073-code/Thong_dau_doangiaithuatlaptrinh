class Solution:
    def countEven(self, num: int) -> int:
        count = 0  # biến dùng để đếm số lượng số có tổng chữ số chẵn
        
        # duyệt từ 1 đến num
        for i in range(1, num + 1):
            
            temp = i      # lưu lại giá trị của i để tách từng chữ số
            digit_sum = 0 # biến lưu tổng các chữ số
            
            # tách từng chữ số của số i
            while temp > 0:
                digit = temp % 10      # lấy chữ số cuối
                digit_sum += digit     # cộng vào tổng
                temp //= 10            # bỏ chữ số cuối
            
            # kiểm tra tổng chữ số có phải số chẵn không
            if digit_sum % 2 == 0:
                count += 1
        
        return count  # trả về kết quả