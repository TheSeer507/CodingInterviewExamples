#Methods to solve the problem
#InOrder, PreOrder,PostOder
#Mantain Complexitu of O(n)
# Number of Nodes in a Perfect Binary Tree 2^level -1
#Start from the root node.
#When Left Extreme level and right extreme level are the same it is a Perfect Binary Tree
#if L and R are not equal then

#Time Complexitu = O(log (2n+1) * log(N+1)) or O(logN * logN)

class Solution:
    def countNodes(self, root):
        if not root
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self,root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)