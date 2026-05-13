# Definition for a binary tree node.
# Đây là class có sẵn của LeetCode
# Không cần sửa

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p, q):

        # Nếu cả 2 node đều rỗng
        # => giống nhau
        if p is None and q is None:
            return True

        # Nếu 1 bên rỗng, 1 bên không
        # => khác nhau
        if p is None or q is None:
            return False

        # Nếu giá trị khác nhau
        # => khác nhau
        if p.val != q.val:
            return False

        # So sánh cây con bên trái
        trai = self.isSameTree(p.left, q.left)

        # So sánh cây con bên phải
        phai = self.isSameTree(p.right, q.right)

        # Chỉ đúng khi cả 2 đều đúng
        return trai and phai