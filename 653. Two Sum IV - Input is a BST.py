# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root, k):

        # Set lưu các số đã gặp
        daGap = set()

        # Hàm duyệt cây
        def duyet(node):

            # Nếu node rỗng
            if node is None:
                return False

            # Số cần tìm
            canTim = k - node.val

            # Nếu đã tồn tại
            if canTim in daGap:
                return True

            # Thêm số hiện tại vào set
            daGap.add(node.val)

            # Duyệt bên trái
            trai = duyet(node.left)

            # Nếu bên trái đã tìm thấy
            if trai:
                return True

            # Duyệt bên phải
            phai = duyet(node.right)

            return phai

        # Bắt đầu duyệt
        return duyet(root)