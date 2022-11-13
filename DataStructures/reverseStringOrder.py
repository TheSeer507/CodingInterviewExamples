#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.

#Approach using two indexes to count the space and the words

class Solution:
    def reverseWords(self, s: str) -> str:
        result, i, n = '', 0, len(s)

        while i < n:
            while i < n and s[i] == ' ': i += 1
            if i >= n: break
            
            j = i + 1
            while j < n and s[j] =='': j += 1
            sub = s[i:j]
            if len (result) == 0: result=sub
            else: result = sub + ' ' + result
            i = j + 1
        return result
