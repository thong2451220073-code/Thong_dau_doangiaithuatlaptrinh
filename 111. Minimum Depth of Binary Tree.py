# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root):
        
        # Nếu cây rỗng → độ sâu = 0
        if not root:
            return 0
        
        # Nếu không có con trái → phải đi bên phải
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # Nếu không có con phải → phải đi bên trái
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # Nếu có cả 2 con → lấy min
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1