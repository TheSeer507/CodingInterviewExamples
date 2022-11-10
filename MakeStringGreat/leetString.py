class Solution:
    def makeGood(self, s: str) -> str:

        #if s has less than 2 characters, we just return itself.
        while len(s) > 1:
            # 'find' records if we find any pair to remove
            find = False

            #Check every pair adjacent characters, curr_char and next_char.

            for i in range(len(s) -1):
                curr_char, next_charr = s[i], s[i+1]

                #if they make pair, remove them from 's' and let find=true
                if abs(ord(curr_char) - ord(next_charr)) == 32:
                    s = s[1:] + s[i + 2:]
                    find = True
                    break

            #If we cannot find ny pair to remove, break the loop.
            if not find:
                break
        
        return s

