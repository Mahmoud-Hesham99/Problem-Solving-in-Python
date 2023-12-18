class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        i = 0
        j = len(nums) - 1 
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                nums[i] = nums[j]
                nums[j] = '_'
                j -= 1
        return i


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    k = Solution().removeElement(nums, val)
    print(nums)
    print(k)