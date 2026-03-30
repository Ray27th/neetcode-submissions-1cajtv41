class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            #Take prefix as number in res
            res[i] = prefix
            #Add on multoplier prefix for next number
            prefix *= nums[i]

        postfix = 1
        #how u start from end to beginning
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i] 

        return(res)