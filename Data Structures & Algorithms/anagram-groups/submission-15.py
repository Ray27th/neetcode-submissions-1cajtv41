class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        output_dict = defaultdict(list)
        
        for s in strs:
            word = [0] * 26
            for letter in s:
                word[ord('a')-ord(letter)] += 1
            
            output_dict[tuple(word)].append(s)

        return list(output_dict.values())