class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Doing modulous here is important, to save repeated iterations
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


        
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)

