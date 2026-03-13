class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Bước 1: đếm
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Bước 2: tìm ký tự đầu tiên có count = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1