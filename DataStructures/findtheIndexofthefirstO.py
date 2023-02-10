class Solution:
    def strStr(self, haystack: str, needle:str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m - n + 1):
            if haystack[i:i + 1] == needle:
                return i
        return -1