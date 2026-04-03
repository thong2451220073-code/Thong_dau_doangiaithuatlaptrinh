class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0  # biến đếm số lần thực hiện
        
        # Lặp cho đến khi 1 trong 2 số = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2  # trừ num2 khỏi num1
            else:
                num2 -= num1  # trừ num1 khỏi num2
            
            count += 1  # tăng số lần
        
        return count