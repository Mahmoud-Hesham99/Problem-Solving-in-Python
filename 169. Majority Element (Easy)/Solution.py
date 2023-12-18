class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        max_count = 0
        majority = 0
        map = {}
        limit = len(nums) // 2
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
            if map[i] > max_count:
                max_count = map[i]
                majority = i
                if max_count > limit:
                    return majority
        return majority
if __name__ == "__main__":
    nums = [3,2,2,3,2]
    k = Solution().majorityElement(nums)
    print(nums)
    print(k)
