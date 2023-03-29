class Solution:
    def romanToInt(self, s: str)-> int:

        roman = {"I" : 1, "V":5, "X":10,
                 "L":50, "C":100, "D":500, "M":1000}
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

#New Solution using Dictionary
#Time O(1)
#Space 0(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        valueSymbols = [(1000, 'M'), (900, 'CM'),
                    (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'),
                    (50, 'L'), (40, 'XL'),
                    (10, 'X'), (9, 'IX'),
                    (5, 'V'), (4, 'IV'),
                    (1, 'I')]
        ans = []

        for value, symbol in valueSymbols:
            if num == 0:
                break
            count, num = divmod(num,value)
            ans.append(symbol * count)
        return ''.join(ans)

    #Solution using Hashtable
    class Solution:
        def intToRoman(self, num: int) -> str:
            M = ['', 'M', 'MM', 'MMM']
            C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
            X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
            I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
            return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]