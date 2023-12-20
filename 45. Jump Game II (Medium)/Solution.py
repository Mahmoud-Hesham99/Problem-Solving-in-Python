class Solution:
    def jump(self, nums: list[int]) -> int:
        #greedy approach since It's guaranteed that you can reach nums[n - 1].
        max_distance = 0
        jumps = 0
        end = 0

        for i in range(len(nums)-1):
            # this indicates the max distance we can reach from i as long i is reachable
            max_distance = max(max_distance, i+nums[i]) 
            
            if i == end:
                jumps += 1
                end = max_distance
                
            if end == len(nums)-1:
                break
        return jumps



        
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    res = Solution().jump(nums)
    print(nums)
    print(res)

