from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        res = []

        for x in arr:
            if x == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(x)

        for i in range(len(arr)):
            arr[i] = res[i]
