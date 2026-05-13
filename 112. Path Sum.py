# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        
        # Nếu cây rỗng → không có đường đi
        if not root:
            return False
        
        # Nếu là leaf (không có con trái và phải)
        if not root.left and not root.right:
            # Kiểm tra tổng có đúng không
            return targetSum == root.val
        
        # Trừ giá trị node hiện tại
        targetSum -= root.val
        
        # Kiểm tra bên trái hoặc bên phải
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
