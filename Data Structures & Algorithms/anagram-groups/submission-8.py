class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        s_dict = defaultdict(list)

        for s in strs:
            word_dict = [0] * 26
            #append into default dict
            for item in s:
                word_dict[ord('a')-ord(item)] += 1

            s_dict[tuple(word_dict)].append(s)

        return list(s_dict.values())
