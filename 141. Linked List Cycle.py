# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x        # giá trị node
        self.next = None    # con trỏ next

class Solution:
    def hasCycle(self, head):
        # Nếu list rỗng hoặc chỉ có 1 phần tử → không có cycle
        if not head or not head.next:
            return False
        
        # Tạo 2 con trỏ
        slow = head        # đi 1 bước
        fast = head        # đi 2 bước
        
        # Lặp khi fast còn đi được
        while fast and fast.next:
            slow = slow.next          # đi 1 bước
            fast = fast.next.next     # đi 2 bước
            
            # Nếu gặp nhau → có cycle
            if slow == fast:
                return True
        
        # Nếu thoát vòng lặp → không có cycle
        return False