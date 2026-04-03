from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Khởi tạo phạm vi tìm kiếm cho vị trí bắt đầu của đoạn con dài k
        left = 0
        right = len(arr) - k  # vì đoạn con dài k nên chỉ số bắt đầu tối đa là len(arr)-k

        # Dùng Binary Search để tìm vị trí bắt đầu phù hợp
        while left < right:
            mid = (left + right) // 2  # lấy chỉ số giữa

            # So sánh khoảng cách từ x đến arr[mid] và arr[mid + k]
            # Nếu arr[mid] xa hơn x so với arr[mid+k] → dịch sang phải
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                # Ngược lại, dịch sang trái (bao gồm mid)
                right = mid

        # Khi vòng lặp kết thúc, left chính là vị trí bắt đầu của đoạn con dài k
        return arr[left:left + k]