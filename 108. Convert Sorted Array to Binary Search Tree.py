# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        
        # Hàm đệ quy tạo cây từ đoạn [left, right]
        def build(left, right):
            
            # Nếu không còn phần tử → trả về None
            if left > right:
                return None
            
            # Chọn phần tử giữa làm root
            mid = (left + right) // 2
            
            # Tạo node root
            root = TreeNode(nums[mid])
            
            # Tạo cây con bên trái
            root.left = build(left, mid - 1)
            
            # Tạo cây con bên phải
            root.right = build(mid + 1, right)
            
            return root
        
        # Gọi hàm với toàn bộ mảng
        return build(0, len(nums) - 1)