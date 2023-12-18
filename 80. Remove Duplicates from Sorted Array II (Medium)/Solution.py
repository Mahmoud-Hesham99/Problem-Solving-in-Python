class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # there is a modified code of the easy version of this problem which is not very elegant, 
        # so here's a better one
        # Here we choose to keep how many duplicates we want to keep using max_n
        max_n = 2 
        x = max_n
        # Just to make sure we handling an edge case where the array is smaller than max_n
        if len(nums) <= max_n:
            return len(nums)
        
        for i in range(max_n,len(nums)):
            if nums[i] != nums[x-max_n] :
                nums[x]=nums[i]
                x+=1
        return x
    
'''
-------------------------------------------------------------------------------------------

'''
        # # This a modfified code of the easy version of this problem
        # i = 0
        # j = 1
        # # n is the number of times a number has appeared
        # n = 1
        # # max_n is the maximum number of times a number can appear and here it's 2
        # max_n = 2
        # # start with 2 pointers, i and j and move j forward until it finds a different number than i
        # while j < len(nums):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        #         n = 1
        #     else:
        #         if n < max_n:
        #             i += 1
        #             nums[i] = nums[j]
        #             n += 1
        #     j += 1

        # # after j reaches the end of the array, we can remove all the duplicates by replacing them with '_'
        # # this is not necessary, but it's to show that the duplicates are removed

        # k = i + 1
        # while k < j:
        #     nums[k] = '_'
        #     k += 1
        # return i + 1 
        
if __name__ == "__main__":
    nums = [1,2,2,2,3,3,4,5,5,5]
    k = Solution().removeDuplicates(nums)
    print(nums)
    print(k)
