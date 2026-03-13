from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # Số tờ tiền $5 hiện đang có
        five = 0
        
        # Số tờ tiền $10 hiện đang có
        ten = 0
        
        # Duyệt qua từng khách hàng trong danh sách bills
        for bill in bills:
            
            # Trường hợp 1: khách trả đúng $5
            # Không cần trả lại tiền thừa
            if bill == 5:
                five += 1   # tăng số tờ $5 lên 1
                
            # Trường hợp 2: khách trả $10
            # Phải trả lại $5
            elif bill == 10:
                
                # Nếu không có tờ $5 để trả lại
                if five == 0:
                    return False   # không thể trả tiền thừa
                
                # Trả lại 1 tờ $5
                five -= 1
                
                # Nhận thêm 1 tờ $10
                ten += 1
                
            # Trường hợp 3: khách trả $20
            # Phải trả lại $15
            else:
                
                # Ưu tiên trả $10 + $5 (để giữ lại nhiều tờ $5)
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                
                # Nếu không có $10 thì trả 3 tờ $5
                elif five >= 3:
                    five -= 3
                
                # Nếu không đủ tiền thừa để trả
                else:
                    return False
        
        # Nếu tất cả khách đều được trả tiền đúng
        return True
