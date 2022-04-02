class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        input_length = len(nums)

        def helper(index, slate):
            if index == input_length:
                solutions.append(list(slate))
                return
            #Exclude case
            helper(nums ,index+1, slate)
            #Include case
            slate.append(nums[index])
            helper(nums, index+1, slate)
            slate.pop()
        helper(0, [])
        return solutions

