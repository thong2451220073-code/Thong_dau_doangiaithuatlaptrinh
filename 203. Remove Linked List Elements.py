# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head, val):
        # Tạo node giả (dummy) có giá trị bất kỳ (0)
        dummy = ListNode(0)
        
        # Cho dummy trỏ tới head ban đầu
        dummy.next = head
        
        # current dùng để duyệt list (bắt đầu từ dummy)
        current = dummy
        
        # Lặp khi còn node phía sau
        while current.next:
            
            # Nếu node phía sau có giá trị cần xóa
            if current.next.val == val:
                
                # BỎ node đó:
                # nối current với node sau của node cần xóa
                current.next = current.next.next
            
            else:
                # Nếu không xóa thì mới di chuyển current
                current = current.next
        
        # Trả về list mới (bỏ dummy)
        return dummy.next