# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Nếu list rỗng thì trả về luôn
        if not head:
            return head
        
        current = head
        
        # Duyệt đến khi còn node tiếp theo
        while current and current.next:
            # Nếu trùng giá trị
            if current.val == current.next.val:
                # Bỏ node phía sau
                current.next = current.next.next
            else:
                # Không trùng thì đi tiếp
                current = current.next
        
        return head