from typing import List   # dùng để khai báo kiểu dữ liệu List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # zip dùng để ghép 2 mảng lại thành từng cặp (height, name)
        # ví dụ: [(180,'Mary'), (165,'John'), (170,'Emma')]
        people = list(zip(heights, names))
        
        # sắp xếp danh sách theo chiều cao giảm dần
        # reverse=True nghĩa là từ lớn → nhỏ
        people.sort(reverse=True)
        
        # tạo danh sách chỉ chứa tên
        # height không cần nên dùng _
        result = [name for height, name in people]
        
        # trả về danh sách tên đã sắp xếp
        return result
