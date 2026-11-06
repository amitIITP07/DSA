class Solution(object):
    def maxPathSum(self, root):

        self.maxi = float('-inf')

        def solve(node):
            if node is None:
                return 0

            leftSum = solve(node.left)
            rightSum = solve(node.right)

            leftSum = max(0, leftSum)
            rightSum = max(0, rightSum)

            self.maxi = max(
                self.maxi,
                leftSum + node.val + rightSum
            )

            return node.val + max(leftSum, rightSum)

        solve(root)
        return self.maxi
        
