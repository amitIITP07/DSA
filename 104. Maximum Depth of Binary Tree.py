class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return 1 + max(leftHeight, rightHeight)
