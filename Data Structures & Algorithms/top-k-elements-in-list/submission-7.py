class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        freq = [[] for x in range(len(nums)+1)]
        res = []

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        for number, count in nums_dict.items():
            freq[count].append(number)

        for i in range(len(freq)-1, -1, -1):
            if freq[i] != []:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res