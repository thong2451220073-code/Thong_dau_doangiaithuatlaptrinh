# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root):

        # Nếu cây rỗng
        if root is None:
            return 0

        # Tổng kết quả
        tong = 0

        # Kiểm tra xem con trái có phải left leaf không
        if root.left:

            # Nếu con trái không có con nào
            if root.left.left is None and root.left.right is None:

                # Cộng giá trị vào tổng
                tong += root.left.val

        # Duyệt tiếp cây bên trái
        tong += self.sumOfLeftLeaves(root.left)

        # Duyệt tiếp cây bên phải
        tong += self.sumOfLeftLeaves(root.right)

        # Trả về kết quả
        return tong