# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []   # list lưu kết quả
        
        # Hàm đệ quy
        def inorder(node):
            # Nếu node rỗng thì dừng
            if not node:
                return
            
            # 1. Đi bên trái
            inorder(node.left)
            
            # 2. Lấy giá trị node
            result.append(node.val)
            
            # 3. Đi bên phải
            inorder(node.right)
        
        # Gọi hàm
        inorder(root)
        
        return result