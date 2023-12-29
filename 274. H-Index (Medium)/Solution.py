class Solution:
    def hIndex(self, citations: list[int]) -> int:

        # if we have a list of 5 elements, the h-index can be at most 5
        # thus if any paper has citations more than the total number of papers, we can ignore it
        # but we need to keep track of how many papers have citations more than the total number of papers
        # since they will be counted as part of the h-index
        more_than_len = 0
        freq_list = [0] * (len(citations)+1)

        # we can use a frequency list to keep track of how many papers have a certain number of citations
        for i in range(len(citations)):
            if citations[i] > len(citations):
                more_than_len += 1 
            else:
                freq_list[citations[i]] += 1
        # we start looping from the end of the array (greater values) since we count them if they are not h-index 
        # but if they are then good 
        papers_that_matters = more_than_len
        for h in range(len(citations), 0, -1):
            papers_that_matters += freq_list[h]
            if papers_that_matters >= h:
                return h
        return 0
            
        # this is the simple solution but with higher complexity
        # citations.sort()
        # n = len(citations)
        # for i in range(n):
        #     if citations[i] >= n - i:
        #         return n - i
        # return 0
        
        return 0
if __name__ == "__main__":
    nums = [3,0,7,1,5]
    k = Solution().hIndex(nums)
    print(nums)
    print(k)
