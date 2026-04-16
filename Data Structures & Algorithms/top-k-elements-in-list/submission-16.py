class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        
        output_arr = [[] for x in range(len(nums)+1)]
        for i in nums:
            nums_dict[i] = nums_dict.get(i,0) + 1
        
        for key, value in nums_dict.items():
            output_arr[value].append(key)
        res = []
        for x in range(len(output_arr)-1,-1,-1):
            if output_arr[x] != []:
                for item in output_arr[x]:
                    res.append(item)
                    if len(res) == k:
                        return res
        