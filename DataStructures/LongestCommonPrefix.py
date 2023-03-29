#Longest Common prefix
#input strinf = ["Flower","Flow","Flight"]
#Output: "fl"
#As these are the common prefix, also check for out of bounds prefix

#Intuition:
#initialize a res variable to store the string value
#Use an i pointer to run through the lenght of the string
#we use another pointer in the string itself to return that res value
#we increment the rest if there are more common values
#we return result

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res