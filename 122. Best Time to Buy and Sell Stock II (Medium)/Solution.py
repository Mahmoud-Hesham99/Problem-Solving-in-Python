class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        #greedy approach
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
            
        return profit


        
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    res = Solution().maxProfit(nums)
    print(nums)
    print(res)

