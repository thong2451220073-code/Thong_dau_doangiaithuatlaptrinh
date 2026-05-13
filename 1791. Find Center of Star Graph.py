class Solution:
    def findCenter(self, edges):

        # Lấy cạnh đầu tiên
        a, b = edges[0]

        # Lấy cạnh thứ hai
        c, d = edges[1]

        # Nếu a xuất hiện ở cạnh thứ hai
        if a == c or a == d:
            return a

        # Ngược lại b là center
        return b