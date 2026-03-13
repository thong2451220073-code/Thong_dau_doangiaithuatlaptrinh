from typing import List   # dùng để khai báo kiểu List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        altitude = 0      # độ cao hiện tại (bắt đầu từ 0)
        highest = 0       # độ cao lớn nhất
        
        # duyệt từng giá trị thay đổi độ cao
        for g in gain:
            
            altitude += g   # cập nhật độ cao hiện tại
            
            # nếu độ cao hiện tại lớn hơn độ cao lớn nhất
            if altitude > highest:
                highest = altitude   # cập nhật độ cao lớn nhất
        
        # trả về độ cao lớn nhất đạt được
        return highest