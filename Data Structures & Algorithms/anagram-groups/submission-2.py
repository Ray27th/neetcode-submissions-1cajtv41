class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        str_dict = defaultdict(list)

        for word in strs:
            str_arr = [0] * 25
            for char in word:
                print(f"char: {char}, ord number: {ord("z")}, ord-a: {ord("z")-ord('a')}")
                str_arr[ord(char)-ord("a")] += 1
            str_dict[tuple(str_arr)].append(word)

        return list(str_dict.values())
        
           
