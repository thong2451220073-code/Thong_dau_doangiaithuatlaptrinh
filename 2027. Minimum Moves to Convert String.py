class Solution:
    def minimumMoves(self, s):

        # Đếm số move
        moves = 0

        # Vị trí hiện tại
        i = 0

        # Duyệt chuỗi
        while i < len(s):

            # Nếu gặp X
            if s[i] == 'X':

                # Cần 1 move
                moves += 1

                # Bỏ qua 3 ký tự
                i += 3

            else:
                # Nếu là O
                i += 1

        return moves