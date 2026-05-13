# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # giá trị của node
        self.next = next    # con trỏ tới node tiếp theo

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Tạo 1 node giả (dummy) để dễ xử lý
        dummy = ListNode()
        
        # con trỏ current dùng để xây dựng list mới
        current = dummy
        
        # Lặp khi cả 2 list còn phần tử
        while list1 and list2:
            # Nếu phần tử list1 nhỏ hơn
            if list1.val < list2.val:
                current.next = list1   # nối node list1 vào
                list1 = list1.next     # di chuyển list1
            else:
                current.next = list2   # nối node list2 vào
                list2 = list2.next     # di chuyển list2
            
            current = current.next     # di chuyển current
        
        # Nếu còn dư list1 thì nối hết vào
        if list1:
            current.next = list1
        
        # Nếu còn dư list2 thì nối hết vào
        if list2:
            current.next = list2
        
        # Trả về list kết quả (bỏ dummy)
        return dummy.next