from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Bước 1: Khởi tạo mảng kết quả với toàn số 0
        # Vì mặc định nếu không có ngày nào ấm hơn thì kết quả là 0
        res = [0] * len(temperatures)

        # Bước 2: Khởi tạo stack để lưu chỉ số các ngày
        # Stack sẽ lưu các ngày có nhiệt độ chưa tìm được ngày ấm hơn
        stack = []

        # Bước 3: Duyệt qua từng ngày
        for i, temp in enumerate(temperatures):
            # Nếu nhiệt độ hiện tại lớn hơn nhiệt độ của ngày ở đỉnh stack
            # thì ta đã tìm được ngày ấm hơn cho ngày đó
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()  # lấy ngày trước đó ra khỏi stack
                res[prev_day] = i - prev_day  # tính số ngày chờ đợi

            # Thêm ngày hiện tại vào stack để chờ tìm ngày ấm hơn
            stack.append(i)

        # Bước 4: Trả về kết quả
        return res