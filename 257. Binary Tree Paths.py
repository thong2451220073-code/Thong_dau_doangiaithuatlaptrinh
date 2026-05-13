# Definition for a binary tree node.
# Đây là class có sẵn của LeetCode
# Không cần sửa

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root):

        # Danh sách lưu kết quả cuối cùng
        ketqua = []

        # Hàm đệ quy duyệt cây
        def duyet(node, duongdi):

            # Nếu node rỗng thì dừng
            if node is None:
                return

            # Thêm giá trị node hiện tại vào đường đi
            if duongdi == "":
                duongdi = str(node.val)
            else:
                duongdi = duongdi + "->" + str(node.val)

            # Nếu là node lá
            # (không có con trái và con phải)
            if node.left is None and node.right is None:

                # Thêm đường đi vào kết quả
                ketqua.append(duongdi)

                return

            # Duyệt cây con bên trái
            duyet(node.left, duongdi)

            # Duyệt cây con bên phải
            duyet(node.right, duongdi)

        # Bắt đầu từ node gốc
        duyet(root, "")

        # Trả về kết quả
        return ketqua