class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Lưu lợi nhuận lớn nhất
        max_profit = 0

        # Vòng lặp chọn ngày mua
        for i in range(len(prices)):

            # Vòng lặp chọn ngày bán (phải sau ngày mua)
            for j in range(i + 1, len(prices)):

                # Tính lợi nhuận nếu mua ngày i và bán ngày j
                profit = prices[j] - prices[i]

                # Nếu lợi nhuận lớn hơn lợi nhuận hiện tại
                if profit > max_profit:
                    max_profit = profit

        # Trả về lợi nhuận lớn nhất
        return max_profit
