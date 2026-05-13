# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        # Nếu list quá ngắn thì không cần làm
        if not head or not head.next:
            return
        
        # ===== BƯỚC 1: TÌM GIỮA =====
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # đi 1 bước
            fast = fast.next.next     # đi 2 bước
        
        # ===== BƯỚC 2: ĐẢO NGƯỢC NỬA SAU =====
        prev = None
        curr = slow.next
        slow.next = None   # cắt list làm 2
        
        while curr:
            next_node = curr.next   # lưu node tiếp theo
            curr.next = prev        # đảo chiều
            prev = curr             # tiến prev
            curr = next_node        # tiến curr
        
        # prev là đầu của list đã đảo (nửa sau)
        
        # ===== BƯỚC 3: TRỘN 2 LIST =====
        first = head       # nửa đầu
        second = prev      # nửa sau
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2