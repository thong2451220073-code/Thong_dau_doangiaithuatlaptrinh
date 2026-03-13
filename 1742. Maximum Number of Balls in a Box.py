class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        box = {}   # dictionary dùng để đếm số bóng trong mỗi hộp
        
        # duyệt tất cả các số bóng
        for i in range(lowLimit, highLimit + 1):
            
            # tính tổng các chữ số của số bóng
            s = sum(int(d) for d in str(i))
            
            # tăng số bóng trong hộp s
            if s in box:
                box[s] += 1
            else:
                box[s] = 1
        
        # trả về số bóng lớn nhất trong các hộp
        return max(box.values())
