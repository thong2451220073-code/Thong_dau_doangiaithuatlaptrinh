# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def checkTree(self, root):

        # Giá trị con trái
        trai = root.left.val

        # Giá trị con phải
        phai = root.right.val

        # Kiểm tra tổng
        return root.val == trai + phai