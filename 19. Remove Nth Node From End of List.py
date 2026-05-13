# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Tạo node giả để xử lý trường hợp xóa node đầu
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # ===== BƯỚC 1: cho fast đi trước n bước =====
        for _ in range(n):
            fast = fast.next
        
        # ===== BƯỚC 2: cùng di chuyển =====
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # ===== BƯỚC 3: xóa node =====
        slow.next = slow.next.next
        
        return dummy.next