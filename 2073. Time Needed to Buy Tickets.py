from typing import List   # dùng để khai báo kiểu dữ liệu List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time = 0   # biến lưu tổng thời gian
        
        # duyệt qua từng người trong hàng
        for i in range(len(tickets)):
            
            # nếu người đó đứng trước hoặc đúng vị trí k
            if i <= k:
                # họ có thể mua tối đa tickets[k] lần
                time += min(tickets[i], tickets[k])
            
            # nếu người đó đứng sau k
            else:
                # họ chỉ mua tối đa tickets[k] - 1 lần
                # vì người k sẽ rời hàng sớm hơn
                time += min(tickets[i], tickets[k] - 1)
        
        # trả về tổng thời gian
        return time
