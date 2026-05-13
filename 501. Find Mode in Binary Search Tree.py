# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root):

        # Dictionary để đếm số lần xuất hiện
        dem = {}

        # Hàm duyệt cây
        def duyet(node):

            # Nếu node rỗng thì dừng
            if node is None:
                return

            # Tăng số lần xuất hiện
            if node.val in dem:
                dem[node.val] += 1
            else:
                dem[node.val] = 1

            # Duyệt trái
            duyet(node.left)

            # Duyệt phải
            duyet(node.right)

        # Bắt đầu duyệt
        duyet(root)

        # Tìm số lần xuất hiện lớn nhất
        lonNhat = max(dem.values())

        # Danh sách kết quả
        ketqua = []

        # Tìm các số có số lần xuất hiện lớn nhất
        for key in dem:

            if dem[key] == lonNhat:
                ketqua.append(key)

        # Trả về kết quả
        return ketqua