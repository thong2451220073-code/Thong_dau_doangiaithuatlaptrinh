class Solution:
    def countPairs(self, nums, k):
        n = len(nums)
        count = 0  # biến đếm số cặp thỏa mãn

        # duyệt tất cả cặp (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                
                # điều kiện 1: giá trị bằng nhau
                if nums[i] == nums[j]:
                    
                    # điều kiện 2: i * j chia hết cho k
                    if (i * j) % k == 0:
                        count += 1  # tăng biến đếm

        return count