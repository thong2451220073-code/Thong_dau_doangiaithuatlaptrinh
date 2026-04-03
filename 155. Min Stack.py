class MinStack:

    def __init__(self):
        # Bước 1: Khởi tạo hai stack
        # stack chính để lưu các giá trị
        self.stack = []
        # min_stack để lưu giá trị nhỏ nhất tại mỗi thời điểm
        self.min_stack = []

    def push(self, val: int) -> None:
        # Bước 2: Thêm giá trị vào stack chính
        self.stack.append(val)
        
        # Bước 3: Nếu min_stack rỗng hoặc val <= giá trị nhỏ nhất hiện tại
        # thì thêm val vào min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Bước 4: Xóa phần tử trên cùng của stack chính
        val = self.stack.pop()
        
        # Nếu phần tử vừa xóa cũng là giá trị nhỏ nhất hiện tại
        # thì xóa nó khỏi min_stack
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Bước 5: Trả về phần tử trên cùng của stack chính
        return self.stack[-1]

    def getMin(self) -> int:
        # Bước 6: Trả về giá trị nhỏ nhất hiện tại từ min_stack
        return self.min_stack[-1]