class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        res = defaultdict(list) #key is character counts of each string e.g. 2 a, 1 b, 1c
        for s in strs:
            count = [0] * 26 #Empty list of 26 0s for a to z

            #Each character
            for char in s:
                count[ord(char) - ord("a")] += 1 #ASCII Values, e.g. a is 80, b i 81, so b will be 1

            #Lists cannot be keys, but tuples can be
            res[tuple(count)].append(s)

        return list(res.values())