class Solution:
    def reverseList(self, head):

        # prev là node trước (ban đầu chưa có)
        prev = None

        # curr là node hiện tại
        curr = head

        # lặp đến khi hết list
        while curr:

            # lưu node tiếp theo
            next_node = curr.next

            # đảo chiều mũi tên
            curr.next = prev

            # di chuyển prev lên
            prev = curr

            # di chuyển curr sang node tiếp
            curr = next_node

        # prev sẽ là head mới
        return prev
