from typing import List   # dùng để khai báo kiểu List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        # tạo mảng kết quả ban đầu, mỗi người 0 viên kẹo
        result = [0] * num_people
        
        give = 1   # số kẹo sẽ phát ở lượt hiện tại
        i = 0      # vị trí người nhận kẹo
        
        # lặp cho đến khi hết kẹo
        while candies > 0:
            
            # nếu số kẹo còn lại ít hơn số cần phát
            # thì phát hết số kẹo còn lại
            result[i % num_people] += min(give, candies)
            
            # trừ số kẹo đã phát
            candies -= give
            
            # tăng số kẹo cho lượt tiếp theo
            give += 1
            
            # chuyển sang người tiếp theo
            i += 1
        
        # trả về mảng kết quả
        return result
