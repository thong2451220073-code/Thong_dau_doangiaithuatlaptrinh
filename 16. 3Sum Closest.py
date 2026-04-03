from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Bước 1: Sắp xếp mảng để dễ dùng kỹ thuật hai con trỏ
        nums.sort()
        
        # Bước 2: Khởi tạo biến kết quả với tổng của 3 phần tử đầu tiên
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Bước 3: Duyệt từng phần tử làm điểm cố định
        for i in range(len(nums) - 2):
            # Khởi tạo hai con trỏ: trái và phải
            left = i + 1
            right = len(nums) - 1
            
            # Bước 4: Dùng kỹ thuật hai con trỏ để tìm tổng gần target nhất
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Nếu tổng hiện tại gần target hơn, cập nhật closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Di chuyển con trỏ dựa trên so sánh với target
                if current_sum < target:
                    left += 1   # tăng tổng bằng cách dịch con trỏ trái sang phải
                elif current_sum > target:
                    right -= 1  # giảm tổng bằng cách dịch con trỏ phải sang trái
                else:
                    # Nếu bằng target thì trả về ngay vì không thể gần hơn nữa
                    return current_sum
        
        # Bước 5: Trả về tổng gần nhất tìm được
        return closest_sum