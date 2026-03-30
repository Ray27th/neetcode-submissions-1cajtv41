class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i

        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i, j = 0, 1
        while i < len(s)-1:
            if s[j] == '#':
                num = int(s[i:j])
                print(num)
                res.append(s[j+1:j+1+num])
                i = j + num + 1
                j = i + 1
            else:
                j += 1

        return res