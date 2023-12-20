class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        max_diff = 0

        for price in prices:

            if price < min:
                min = price

            profit = price - min

            if profit > max_diff:
                max_diff = profit
            
        return max_diff
        
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    res = Solution().maxProfit(nums)
    print(res)

