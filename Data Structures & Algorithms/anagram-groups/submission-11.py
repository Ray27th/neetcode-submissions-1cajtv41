class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res_dict = defaultdict(list)

        for s in strs:
            word = [0] * 26
            for item in s:
                word[ord('a')-ord(item)] += 1

            res_dict[tuple(word)].append(s)

        return list(res_dict.values())