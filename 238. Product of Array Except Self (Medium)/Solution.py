import random
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        res = [0]*n
        # the trick here is to iterate twice calculating the prefix product and postfix product
        # then multiply the prefix product with the postfix product to get the result in O(n) time 
        # without using division
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= postfix_product
            postfix_product *= nums[i]
        return res





if __name__ == "__main__":
    obj = Solution()
    res = obj.productExceptSelf([1,2,3,4])
    print(res)