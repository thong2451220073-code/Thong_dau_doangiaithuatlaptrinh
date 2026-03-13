from collections import Counter
from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        # Đếm số lần xuất hiện của mỗi từ trong words1
        count1 = Counter(words1)
        
        # Đếm số lần xuất hiện của mỗi từ trong words2
        count2 = Counter(words2)
        
        result = 0  # biến lưu số từ thỏa điều kiện
        
        # duyệt từng từ trong words1
        for word in count1:
            
            # nếu từ xuất hiện đúng 1 lần trong cả 2 mảng
            if count1[word] == 1 and count2[word] == 1:
                result += 1
        
        return result