class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        highest_profit = 0

        prices_len = len(prices)

        if prices_len == 1: return profit

        for i in range(prices_len):
            if i == prices_len - 1: break

            for j in range(i, prices_len):
                print(f'entered the loop {i} {j}')
                if i == j: continue
                if prices[i] > prices[j]: break

                op_value = prices[j] - prices[i]
                if op_value > profit:
                    profit = op_value


        return profit

            
            # [5,2,3,4,3,8,1,9]
            