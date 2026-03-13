from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_words = 0  # lưu số từ lớn nhất
        
        for s in sentences:  # duyệt từng câu
            
            words = s.split()  # tách câu thành các từ
            
            max_words = max(max_words, len(words))  # cập nhật số lớn nhất
        
        return max_words
