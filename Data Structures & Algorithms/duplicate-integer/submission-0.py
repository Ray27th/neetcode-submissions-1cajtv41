class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage_arr = []

        for i in nums:
            if i not in storage_arr:
                storage_arr.append(i)
            else:
                return True

        return False