from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0  # biến đếm số từ có prefix
        
        # duyệt từng từ trong danh sách
        for word in words:
            # kiểm tra từ có bắt đầu bằng pref không
            if word.startswith(pref):
                count += 1
        
        return count

