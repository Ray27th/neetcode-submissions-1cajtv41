class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[count/frequency]
        #[index]
        freq = [[] for x in range(len(nums)+1)]

        nums_dict = {}
        res = []

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        print(nums_dict)

        for num, count in nums_dict.items():
            print(f'num:{num} and count{count}')
            freq[count].append(num)

        for i in range(len(freq)-1, -1, -1):
            print(freq[i])
            if freq[i] != []:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
