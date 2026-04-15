class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for i in s:
            s_dict[i] = s_dict.get(i,0) + 1

        for i in t:
            t_dict[i] = t_dict.get(i,0) + 1

        if s_dict == t_dict:
            return True
        else:
            return False