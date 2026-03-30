class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, 1

        while i < n:
            if nums[i] + nums[j] == target:
                return [i,j]
            else:
                #Loop second pointer
                j += 1
                #Once second pointer out of bounds
                if j > (n-1):
                    i += 1
                    j = i + 1
        
