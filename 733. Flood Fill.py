class Solution:
    def floodFill(self, image, sr, sc, color):

        # Số hàng
        rows = len(image)

        # Số cột
        cols = len(image[0])

        # Màu gốc
        mauCu = image[sr][sc]

        # Nếu màu mới giống màu cũ
        if mauCu == color:
            return image

        # Hàm DFS
        def dfs(r, c):

            # Nếu ra ngoài ma trận
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # Nếu khác màu gốc
            if image[r][c] != mauCu:
                return

            # Đổi màu
            image[r][c] = color

            # Đi lên
            dfs(r - 1, c)

            # Đi xuống
            dfs(r + 1, c)

            # Đi trái
            dfs(r, c - 1)

            # Đi phải
            dfs(r, c + 1)

        # Bắt đầu DFS
        dfs(sr, sc)

        # Trả về ảnh
        return image