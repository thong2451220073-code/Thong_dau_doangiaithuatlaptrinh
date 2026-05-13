class Solution:
    def addTwoNumbers(self, l1, l2):

        # Node giả để bắt đầu list kết quả
        dummy = ListNode(0)

        # Con trỏ để xây dựng list mới
        current = dummy

        # Biến nhớ khi cộng >=10
        carry = 0

        # Lặp khi còn node hoặc còn số nhớ
        while l1 or l2 or carry:

            # Lấy giá trị node (nếu không có thì =0)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Tính tổng
            total = v1 + v2 + carry

            # Cập nhật số nhớ
            carry = total // 10

            # Giá trị node mới
            digit = total % 10

            # Tạo node mới
            current.next = ListNode(digit)

            # Di chuyển con trỏ
            current = current.next

            # Di chuyển l1
            if l1:
                l1 = l1.next

            # Di chuyển l2
            if l2:
                l2 = l2.next

        # Trả về kết quả
        return dummy.next
