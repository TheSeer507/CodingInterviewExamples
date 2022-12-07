#Explanation:
#why using zip ?
#=> zip function would pair the first item of first iterator (i.e s here) to the first item of second iterator (i.e t here). set()
# would remove duplicate items from the zipped tuple. It is like the first item of first iterator mapped to the first item of second iterator
# as it would in case of a hashtable or dictionary.
#Understand using exmaples:

# when strings ae isomorphic:
#s = "egg"
#t = "add"

def example1(s,d):
    zipped_set = {('e', 'a'), ('g', 'd')}
    # now comparing their lengths when duplicacies are removed
    return len(zipped_set) == len(set(s)) == len(set(d))
    # return 2 == 2 == 2 -> True

# when strings are not isomorphic:
#s = "egk"
#t = "add"

def example2(s,d):
    zipped_set = {('e', 'a'), ('g', 'd'), ('k', 'd')}
    # now comparing their lengths when duplicacies are removed
    return len(zipped_set) == len(set(s)) == len(set(d))
    # return 3 == 3 == 2 -> False


class Solution:
    def isIsomorphic(self,s: str, t:str) -> bool:
        zipped_set = set(zip(s,t))
        return len(zipped_set) == len(set(s)) == len(set(t))