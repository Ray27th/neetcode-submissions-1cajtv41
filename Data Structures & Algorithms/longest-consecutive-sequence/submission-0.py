class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #make it a set, so every check if O(1)
        numSet = set(nums)
        longest = 0

        #Iterate the array
        for n in nums:
            #Check if start of sequence (if they got a left)
            if (n - 1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest