class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        res = []
        
        #Count frequency in nums array
        for i in nums:
            #Put it in a nums_dictionary
            nums_dict[i] = nums_dict.get(i, 0) + 1
        
        max_key = 0
        max_freq = 0
        #Loop k frequence
        for i in range(k):
            for key, freq in nums_dict.items():
                #Its not entering for second loop?
                if key not in res and freq > max_freq:
                    max_freq = freq
                    max_key = key

            print(nums_dict)
            print(max_key)
            res.append(max_key)
            max_key = 0
            max_freq = 0

        return res
            