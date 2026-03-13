class Solution:
    def reformatNumber(self, number: str) -> str:
        
        # xóa dấu cách và dấu -
        digits = number.replace(" ", "").replace("-", "")
        
        res = []   # danh sách lưu các nhóm số
        i = 0      # vị trí hiện tại
        
        # lặp cho đến khi hết số
        while len(digits) - i > 4:
            # lấy nhóm 3 số
            res.append(digits[i:i+3])
            i += 3
        
        # xử lý phần còn lại
        remain = len(digits) - i
        
        if remain == 4:
            # chia thành 2 nhóm 2
            res.append(digits[i:i+2])
            res.append(digits[i+2:i+4])
        else:
            # nếu còn 2 hoặc 3 số
            res.append(digits[i:])
        
        # nối các nhóm bằng dấu -
        return "-".join(res)
