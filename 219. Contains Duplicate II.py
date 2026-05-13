class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        # Tạo dictionary để lưu:
        # key = giá trị trong mảng
        # value = vị trí xuất hiện gần nhất
        dic = {}

        # Duyệt từng phần tử trong mảng bằng index i
        for i in range(len(nums)):

            # Nếu số hiện tại đã từng xuất hiện
            if nums[i] in dic:

                # Tính khoảng cách giữa vị trí hiện tại và vị trí trước đó
                if i - dic[nums[i]] <= k:
                    return True   # nếu ≤ k thì thỏa điều kiện

            # Cập nhật lại vị trí mới nhất của số đó
            dic[nums[i]] = i

        # Nếu duyệt hết mà không tìm thấy
        return False
