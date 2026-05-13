# Definition for a binary tree node.
# Đây là class có sẵn của LeetCode
# Không cần sửa

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root):

        # Danh sách lưu kết quả
        ketqua = []

        # Hàm đệ quy duyệt cây
        def duyet(node):

            # Nếu node rỗng thì dừng
            if node is None:
                return

            # 1. Duyệt cây con bên trái
            duyet(node.left)

            # 2. Duyệt cây con bên phải
            duyet(node.right)

            # 3. Thêm node gốc vào kết quả
            ketqua.append(node.val)

        # Bắt đầu duyệt từ node gốc
        duyet(root)

        # Trả về kết quả
        return ketqua