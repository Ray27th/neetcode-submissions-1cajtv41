class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        output_dict = defaultdict(list)
        
        for word in strs:
            check = [0] * 26
            for letter in word:
                check[ord('a')-ord(letter)] += 1
            
            output_dict[tuple(check)].append(word)

        return list(output_dict.values())   



