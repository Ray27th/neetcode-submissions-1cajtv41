class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array_check = [[] for x in range(len(nums)+1)]
        nums_dict = {}

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        for key, value in nums_dict.items():
            array_check[value].append(key)

        res = []
        for x in range(len(array_check)-1, -1, -1):
            if array_check[x] != []:
                for item in array_check[x]:
                    res.append(item)
                    if len(res) == k:
                        return res