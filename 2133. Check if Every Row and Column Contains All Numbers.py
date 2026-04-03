class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        
        # Tập chuẩn từ 1 -> n
        target = set(range(1, n + 1))
        
        # Kiểm tra từng hàng
        for row in matrix:
            if set(row) != target:
                return False
        
        # Kiểm tra từng cột
        for col in range(n):
            column = []
            for row in range(n):
                column.append(matrix[row][col])
            
            if set(column) != target:
                return False
        
        return True
