class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        print(sett)
        max_seq = []
        res = 0

        for i in nums:
            print(i)
            if i-1 not in sett:
                print('working?')
                max_seq.append(i)
                print(f'max_seq: {max_seq}')
                while i+1 in sett:
                    max_seq.append(i+1)
                    i = i+1

                res = max(len(max_seq), res)
                max_seq = []
                print(f'res: {res}')
        
        return res