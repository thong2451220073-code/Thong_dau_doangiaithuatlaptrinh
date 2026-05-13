# Definition for a binary tree node.
# Đây là class có sẵn của LeetCode
# Không cần sửa

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root):

        # Nếu cây rỗng thì trả về luôn
        if root is None:
            return None

        # Đổi chỗ cây con trái và phải
        temp = root.left
        root.left = root.right
        root.right = temp

        # Đảo cây con bên trái
        self.invertTree(root.left)

        # Đảo cây con bên phải
        self.invertTree(root.right)

        # Trả về node gốc
        return root