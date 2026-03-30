class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        i, j = 0, 1

        while i < len(nums):
            if nums[j] == target - nums[i] and i!=j:
                return [i, j]
            else: 
                j += 1 
                if j >= len(nums):
                    j = i + 1
                    i += 1
            