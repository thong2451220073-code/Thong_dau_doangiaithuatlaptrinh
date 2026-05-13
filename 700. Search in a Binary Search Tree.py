# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def searchBST(self, root, val):

        # Nếu cây rỗng
        if root is None:
            return None

        # Nếu tìm thấy node
        if root.val == val:
            return root

        # Nếu val nhỏ hơn root
        # tìm bên trái
        if val < root.val:
            return self.searchBST(root.left, val)

        # Nếu val lớn hơn root
        # tìm bên phải
        return self.searchBST(root.right, val)