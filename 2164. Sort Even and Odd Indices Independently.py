from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Bước 1: Lấy các phần tử ở vị trí chẵn
        even = []
        # Bước 2: Lấy các phần tử ở vị trí lẻ
        odd = []
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])  # index chẵn
            else:
                odd.append(nums[i])   # index lẻ
        
        # Bước 3: Sắp xếp
        even.sort()            # tăng dần
        odd.sort(reverse=True) # giảm dần
        
        # Bước 4: Ghép lại
        e = 0  # con trỏ even
        o = 0  # con trỏ odd
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1
        
        # Bước 5: Trả về kết quả
        return nums