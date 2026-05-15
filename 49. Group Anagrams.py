from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))  # sắp xếp chữ cái
            mp[key].append(s)         # gom vào nhóm

        return list(mp.values())