class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count: [0] [1] [2] [3] [4] [5] [6]
        # Freq:  [0] [1] [2] [3] [0] [0] [0]

        array_track = [[] for x in range(len(nums)+1)]
        print(array_track)
        nums_dict = {}

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        for key, value in nums_dict.items():
            array_track[value].append(key)

        print(array_track)

        output = []
        for x in range(len(array_track)-1, -1, -1):
            if array_track[x] != []:
                for item in array_track[x]:
                    output.append(item)
                    if len(output) == k:
                        return output