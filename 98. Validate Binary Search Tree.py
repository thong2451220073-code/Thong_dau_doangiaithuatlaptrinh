# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root):

        # Hàm kiểm tra BST
        def kiemtra(node, minn, maxx):

            # Nếu node rỗng
            # => đúng
            if node is None:
                return True

            # Nếu giá trị không nằm trong khoảng cho phép
            if node.val <= minn or node.val >= maxx:
                return False

            # Kiểm tra cây bên trái
            trai = kiemtra(node.left, minn, node.val)

            # Kiểm tra cây bên phải
            phai = kiemtra(node.right, node.val, maxx)

            # Cả 2 đều đúng thì mới đúng
            return trai and phai

        # Ban đầu:
        # min = -∞
        # max = +∞
        return kiemtra(root, float('-inf'), float('inf'))