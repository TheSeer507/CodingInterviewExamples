#Check wether a number is a palindrome
# example 121 = True
#Print True if true or false if false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x)[::1]:
            return True
        else:
            return False
