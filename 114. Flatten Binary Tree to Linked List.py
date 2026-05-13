# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root):

        # Nếu cây rỗng thì dừng
        if not root:
            return

        # Flatten cây con bên trái
        self.flatten(root.left)

        # Flatten cây con bên phải
        self.flatten(root.right)

        # Lưu cây bên phải lại
        temp = root.right

        # Đưa cây bên trái sang bên phải
        root.right = root.left

        # Xóa nhánh trái
        root.left = None

        # Tìm node cuối bên phải
        current = root
        while current.right:
            current = current.right

        # Gắn cây phải cũ vào cuối
        current.right = temp