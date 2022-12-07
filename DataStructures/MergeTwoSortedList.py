





class Solution:
    def mergeTwoList(self,a,b):
        if a and b:
            if a.val > b.val:
                a,b = b,a
            a.next = self.mergeTwoList(a.next,b)
        return a or b