from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = len(set(candyType))
        return min(types, len(candyType) // 2)
