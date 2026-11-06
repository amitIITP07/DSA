class Solution(object):
    def rightSideView(self, root):

        ans = []

        def solve(node, level):
            if node is None:
                return

            if len(ans) == level:
                ans.append(node.val)

            solve(node.right, level + 1)
            solve(node.left, level + 1)

        solve(root, 0)

        return ans
        
