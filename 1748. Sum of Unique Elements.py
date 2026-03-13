from typing import List   # khai báo kiểu List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        count = {}   # dictionary dùng để đếm số lần xuất hiện
        
        # duyệt từng số trong mảng
        for n in nums:
            if n in count:
                count[n] += 1   # nếu đã có thì tăng số lần
            else:
                count[n] = 1    # nếu chưa có thì thêm vào
        
        total = 0   # biến lưu tổng các số xuất hiện đúng 1 lần
        
        # duyệt lại dictionary
        for key in count:
            if count[key] == 1:   # nếu xuất hiện đúng 1 lần
                total += key      # cộng vào tổng
        
        return total   # trả kết quả
