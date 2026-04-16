class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + '#' + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 1
        while i < len(s)-1:
            if s[j] == '#':
                num = int(s[i:j])
                print(num)
                res.append(s[j+1:j+1+num])
                i = j+1+num
                j = i + 1
            else:
                j += 1

        return res
