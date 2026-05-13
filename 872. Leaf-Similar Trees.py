# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1, root2):

        # Hàm lấy danh sách leaf
        def layLeaf(node, danhSach):

            # Nếu node rỗng
            if node is None:
                return

            # Nếu là leaf
            if node.left is None and node.right is None:

                # Thêm vào danh sách
                danhSach.append(node.val)

                return

            # Duyệt cây trái
            layLeaf(node.left, danhSach)

            # Duyệt cây phải
            layLeaf(node.right, danhSach)

        # Danh sách leaf cây 1
        leaf1 = []

        # Danh sách leaf cây 2
        leaf2 = []

        # Lấy leaf cây 1
        layLeaf(root1, leaf1)

        # Lấy leaf cây 2
        layLeaf(root2, leaf2)

        # So sánh 2 danh sách
        return leaf1 == leaf2