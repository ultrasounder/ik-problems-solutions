class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        input_length  = len(nums)
        solutions = []

        def helper(nums, index, slate):
            if index == input_length:
                solutions.append(slate[:])
                return
            for pick in range(index, input_length-1):
                slate[pick], slate[index] = slate[index], slate[pick]
                slate.append(nums[index])
                helper(nums, index +1, slate)
                slate.pop()
        helper(nums, 0, [])
        return solutions