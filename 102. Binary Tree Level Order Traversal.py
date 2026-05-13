from collections import deque

class Solution:
    def levelOrder(self, root):

        # Nếu cây rỗng
        if root is None:
            return []

        # Danh sách kết quả
        ketqua = []

        # Tạo queue
        queue = deque()

        # Đưa node gốc vào queue
        queue.append(root)

        # Khi queue còn phần tử
        while queue:

            # Số node của tầng hiện tại
            soNode = len(queue)

            # Lưu các node của tầng hiện tại
            tang = []

            # Duyệt hết node trong tầng
            for i in range(soNode):

                # Lấy node đầu queue
                node = queue.popleft()

                # Thêm giá trị node vào tầng
                tang.append(node.val)

                # Nếu có con trái
                if node.left:
                    queue.append(node.left)

                # Nếu có con phải
                if node.right:
                    queue.append(node.right)

            # Thêm tầng vào kết quả
            ketqua.append(tang)

        # Trả về kết quả
        return ketqua