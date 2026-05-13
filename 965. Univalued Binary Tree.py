# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root):

        # Giá trị chuẩn để so sánh
        giaTri = root.val

        # Hàm duyệt cây
        def duyet(node):

            # Nếu node rỗng
            if node is None:
                return True

            # Nếu khác giá trị chuẩn
            if node.val != giaTri:
                return False

            # Kiểm tra trái
            trai = duyet(node.left)

            # Kiểm tra phải
            phai = duyet(node.right)

            # Cả 2 đều đúng mới đúng
            return trai and phai

        # Bắt đầu duyệt
        return duyet(root)