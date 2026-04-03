class Solution:
    def minimumCost(self, cost):
        # Sắp xếp giảm dần
        cost.sort(reverse=True)
        
        total = 0
        
        # Duyệt từng phần tử
        for i in range(len(cost)):
            
            # Nếu là phần tử thứ 3 (i % 3 == 2) → miễn phí
            if i % 3 == 2:
                continue
            
            # Ngược lại thì cộng tiền
            total += cost[i]
        
        return total