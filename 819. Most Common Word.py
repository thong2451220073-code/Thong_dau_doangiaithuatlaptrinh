from collections import Counter
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        
        words = re.findall(r"[a-z]+", paragraph)
        
        count = Counter(words)
        
        for word in banned:
            count.pop(word, None)
        
        return count.most_common(1)[0][0]