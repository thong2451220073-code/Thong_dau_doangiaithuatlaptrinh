class Solution:
    def numIslands(self, grid):

        # Số hàng
        rows = len(grid)

        # Số cột
        cols = len(grid[0])

        # Đếm số đảo
        dem = 0

        # Hàm DFS để xóa đảo
        def dfs(r, c):

            # Nếu ra ngoài ma trận
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # Nếu là nước
            if grid[r][c] == "0":
                return

            # Đánh dấu đã thăm
            grid[r][c] = "0"

            # Đi lên
            dfs(r - 1, c)

            # Đi xuống
            dfs(r + 1, c)

            # Đi trái
            dfs(r, c - 1)

            # Đi phải
            dfs(r, c + 1)

        # Duyệt toàn bộ ma trận
        for r in range(rows):
            for c in range(cols):

                # Nếu gặp đất
                if grid[r][c] == "1":

                    # Tìm thấy đảo mới
                    dem += 1

                    # Xóa toàn bộ đảo
                    dfs(r, c)

        # Trả về kết quả
        return dem