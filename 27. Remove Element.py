from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Bước 1: Khởi tạo con trỏ index để ghi đè các phần tử khác val
        index = 0
        
        # Bước 2: Duyệt qua từng phần tử trong mảng nums
        for i in range(len(nums)):
            # Nếu phần tử hiện tại khác với val (không cần xóa)
            if nums[i] != val:
                # Ghi đè phần tử này vào vị trí index
                nums[index] = nums[i]
                # Tăng index lên để chuẩn bị cho phần tử tiếp theo
                index += 1
        
        # Bước 3: Sau khi duyệt xong, index chính là số phần tử còn lại (không bằng val)
        return index