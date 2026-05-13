class Solution:
    def islandPerimeter(self, grid):

        # Số hàng
        rows = len(grid)

        # Số cột
        cols = len(grid[0])

        # Chu vi
        chuVi = 0

        # Duyệt toàn bộ ma trận
        for r in range(rows):
            for c in range(cols):

                # Nếu là đất
                if grid[r][c] == 1:

                    # Ban đầu mỗi ô có 4 cạnh
                    chuVi += 4

                    # Kiểm tra ô phía trên
                    if r > 0 and grid[r - 1][c] == 1:
                        chuVi -= 1

                    # Kiểm tra ô phía dưới
                    if r < rows - 1 and grid[r + 1][c] == 1:
                        chuVi -= 1

                    # Kiểm tra ô bên trái
                    if c > 0 and grid[r][c - 1] == 1:
                        chuVi -= 1

                    # Kiểm tra ô bên phải
                    if c < cols - 1 and grid[r][c + 1] == 1:
                        chuVi -= 1

        # Trả về kết quả
        return chuVi