class Solution:
    def canJump(self, nums: list[int]) -> bool:
        #greedy approach
        max_distance = 0

        for i in range(len(nums)):

            if i>max_distance:
                return False # if i is not reachable, then return False
            
            # this indicates the max distance we can reach from i as long i is reachable
            max_distance = max(max_distance, i+nums[i]) 
            
            if max_distance >= len(nums)-1:
                return True


        
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    res = Solution().canJump(nums)
    print(nums)
    print(res)

