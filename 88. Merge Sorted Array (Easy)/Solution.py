class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # set pointers to the end of each array
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            # since arrays are sorted, we can compare the last elements of each array
            # and add the larger one to the end of nums1 array and decrement the pointer
            # of the array that had the larger element 
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0,0]
    m = 3
    nums2 = [1,2,5,6] 
    n = 4
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
