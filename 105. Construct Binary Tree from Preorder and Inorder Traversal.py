# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder, inorder):

        # Nếu mảng rỗng
        # => không có cây
        if not preorder or not inorder:
            return None

        # Phần tử đầu preorder là root
        rootVal = preorder[0]

        # Tạo node gốc
        root = TreeNode(rootVal)

        # Tìm vị trí root trong inorder
        index = inorder.index(rootVal)

        # Các phần tử bên trái index
        # là cây con trái
        inorderTrai = inorder[:index]

        # Các phần tử bên phải index
        # là cây con phải
        inorderPhai = inorder[index + 1:]

        # Số node bên trái
        soLuongTrai = len(inorderTrai)

        # Preorder của cây trái
        preorderTrai = preorder[1:1 + soLuongTrai]

        # Preorder của cây phải
        preorderPhai = preorder[1 + soLuongTrai:]

        # Dựng cây trái
        root.left = self.buildTree(preorderTrai, inorderTrai)

        # Dựng cây phải
        root.right = self.buildTree(preorderPhai, inorderPhai)

        # Trả về root
        return root