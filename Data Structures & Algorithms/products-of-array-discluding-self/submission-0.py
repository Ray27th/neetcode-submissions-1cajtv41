class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            left = nums[:i]
            print(f'left: {left}')
            right = nums[i+1:]
            print(f'right: {right}')
            prod_arr = left+right
            print(f'prod_arr: {prod_arr}')
            prod=1
            for i in prod_arr:
                prod *= i

            res.append(prod)
            prod = 0
        
        return res                       