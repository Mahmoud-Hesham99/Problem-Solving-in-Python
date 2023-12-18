class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1
        # start with 2 pointers, i and j and move j forward until it finds a different number than i
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1

        # after j reaches the end of the array, we can remove all the duplicates by replacing them with '_'
        # this is not necessary, but it's to show that the duplicates are removed
        k = i + 1
        while k < j:
            nums[k] = '_'
            k += 1
        return i + 1 


if __name__ == "__main__":
    nums = [1,2,2,2,3,3,4,5]
    k = Solution().removeDuplicates(nums)
    print(nums)
    print(k)
