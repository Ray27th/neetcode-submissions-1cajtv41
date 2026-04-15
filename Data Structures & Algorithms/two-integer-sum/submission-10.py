class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        while i < len(nums):
            if target - nums[i] == nums[j]:
                return [i,j]
            else:
                j += 1
                if j == len(nums):
                    i += 1
                    j = i + 1

        