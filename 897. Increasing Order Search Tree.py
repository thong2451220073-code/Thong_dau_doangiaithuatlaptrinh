# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root):

        # Node giả để dễ nối
        dummy = TreeNode(0)

        # Con trỏ hiện tại
        self.current = dummy

        # Hàm inorder
        def inorder(node):

            # Nếu node rỗng
            if node is None:
                return

            # Duyệt trái
            inorder(node.left)

            # Xóa con trái
            node.left = None

            # Nối node hiện tại vào bên phải
            self.current.right = node

            # Di chuyển current
            self.current = node

            # Duyệt phải
            inorder(node.right)

        # Bắt đầu inorder
        inorder(root)

        # Trả về cây mới
        return dummy.right