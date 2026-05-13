# Definition for a binary tree node.
# Đây là class có sẵn của LeetCode
# Không cần sửa

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root):

        # Nếu cây rỗng
        # độ sâu = 0
        if root is None:
            return 0

        # Tính độ sâu cây con bên trái
        trai = self.maxDepth(root.left)

        # Tính độ sâu cây con bên phải
        phai = self.maxDepth(root.right)

        # Lấy lớn nhất rồi cộng thêm node hiện tại
        return max(trai, phai) + 1