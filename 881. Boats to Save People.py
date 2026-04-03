from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Bước 1: Sắp xếp danh sách trọng lượng từ nhỏ đến lớn
        people.sort()
        
        # Bước 2: Khởi tạo hai con trỏ
        left = 0                # chỉ số người nhẹ nhất
        right = len(people) - 1 # chỉ số người nặng nhất
        
        # Bước 3: Biến đếm số thuyền cần dùng
        boats = 0
        
        # Bước 4: Duyệt cho đến khi tất cả mọi người đều được xếp lên thuyền
        while left <= right:
            # Nếu người nhẹ nhất + người nặng nhất <= giới hạn,
            # thì có thể ghép họ chung một thuyền
            if people[left] + people[right] <= limit:
                left += 1       # người nhẹ nhất đã lên thuyền
                right -= 1      # người nặng nhất cũng đã lên thuyền
            else:
                # Nếu không thể ghép, thì người nặng nhất phải đi một mình
                right -= 1
            
            # Dù ghép được hay không, vẫn cần thêm một thuyền
            boats += 1
        
        # Bước 5: Trả về tổng số thuyền đã dùng
        return boats