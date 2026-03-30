class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + '#' + i

        return res

    def decode(self, s: str) -> List[str]:
        #Set two pointers to find number & #
        i, j = 0, 1
        res = []
        #Loop thru character
        while i < len(s) and j < len(s):
            print(s)
            print(len(s))
            if s[j] == '#':
                num = int(s[i:j])
                print(f'num: {num}')
                res.append(s[j+1:j+1+num])
                print(f'res: {res}')
                i = j+num+1
                j = i + 1
            else:
                j += 1

        return res
