from typing import List   # khai báo kiểu List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0   # biến đếm số item thỏa điều kiện
        
        # duyệt từng item trong danh sách
        for item in items:
            
            # kiểm tra theo từng rule
            if ruleKey == "type" and item[0] == ruleValue:
                count += 1
            
            elif ruleKey == "color" and item[1] == ruleValue:
                count += 1
            
            elif ruleKey == "name" and item[2] == ruleValue:
                count += 1
        
        # trả về số item thỏa điều kiện
        return count
