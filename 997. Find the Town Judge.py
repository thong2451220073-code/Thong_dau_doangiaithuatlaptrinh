class Solution:
    def findJudge(self, n, trust):

        # Số người tin mình
        inDegree = [0] * (n + 1)

        # Mình tin bao nhiêu người
        outDegree = [0] * (n + 1)

        # Duyệt danh sách trust
        for a, b in trust:

            # a tin b

            # a tin thêm 1 người
            outDegree[a] += 1

            # b được thêm 1 người tin
            inDegree[b] += 1

        # Kiểm tra từng người
        for i in range(1, n + 1):

            # Điều kiện judge
            if inDegree[i] == n - 1 and outDegree[i] == 0:
                return i

        # Không có judge
        return -1