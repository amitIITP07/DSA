class Solution(object):

    def solve(self, root, limit):

        if root is None:
            return True

        if not limit[0] < root.val < limit[1]:
            return False

        left = self.solve(root.left, [limit[0], root.val])

        if left == False:
            return False

        right = self.solve(root.right, [root.val, limit[1]])

        return left and right

    def isValidBST(self, root):
        return self.solve(root, [float('-inf'), float('inf')])
