# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # Hàm kiểm tra 2 cây có giống nhau không
    def giongNhau(self, a, b):

        # Nếu cả 2 đều rỗng
        if a is None and b is None:
            return True

        # Nếu 1 bên rỗng
        if a is None or b is None:
            return False

        # Nếu giá trị khác nhau
        if a.val != b.val:
            return False

        # So sánh tiếp trái và phải
        return (self.giongNhau(a.left, b.left)
                and
                self.giongNhau(a.right, b.right))


    def isSubtree(self, root, subRoot):

        # Nếu root rỗng
        if root is None:
            return False

        # Nếu cây hiện tại giống subRoot
        if self.giongNhau(root, subRoot):
            return True

        # Kiểm tra bên trái hoặc bên phải
        return (self.isSubtree(root.left, subRoot)
                or
                self.isSubtree(root.right, subRoot))