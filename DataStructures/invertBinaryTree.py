<<<<<<< HEAD
#Invert a binary tree
#pay attention to the subtree

#We can use DFS to solve the problem recursively

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#Shortest solution
    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if (root == None): return
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
=======
#Invert a binary tree
#pay attention to the subtree

#We can use DFS to solve the problem recursively

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#Shortest solution
    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if (root == None): return
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
>>>>>>> 1f12b88269c68e4e1b02aa59849a43f9ea5c59a0
            return root