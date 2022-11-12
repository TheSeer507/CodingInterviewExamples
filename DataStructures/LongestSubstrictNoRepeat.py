<<<<<<< HEAD
#Given a string s find the longest substring without repeating characters
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lenghtOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res =  max(res, r -l + 1)
        return res
    # @param s, a string
    # @return an integer
=======
#Given a string s find the longest substring without repeating characters
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lenghtOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res =  max(res, r -l + 1)
        return res
    # @param s, a string
    # @return an integer
>>>>>>> 1f12b88269c68e4e1b02aa59849a43f9ea5c59a0
