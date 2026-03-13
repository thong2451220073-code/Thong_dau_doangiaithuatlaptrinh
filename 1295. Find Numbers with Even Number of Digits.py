from typing import List   # dùng để khai báo kiểu List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0   # biến dùng để đếm số có chữ số chẵn
        
        # duyệt từng số trong mảng
        for n in nums:
            
            # chuyển số thành chuỗi để đếm số chữ số
            digits = len(str(n))
            
            # nếu số chữ số là số chẵn
            if digits % 2 == 0:
                count += 1   # tăng biến đếm
        
        # trả về kết quả
        return count
