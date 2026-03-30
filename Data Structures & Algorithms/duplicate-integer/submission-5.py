class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}

        for i in nums:
            dup_dict[i] = dup_dict.get(i, 0) + 1
            if dup_dict[i] == 2:
                return True
        
        return False