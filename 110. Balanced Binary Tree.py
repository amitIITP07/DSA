class Solution(object):
    def isBalanced(self, root):

        def solve(node):
            if node == None:
                return 0

            LH = solve(node.left)
            if LH == -1:
                return -1

            RH = solve(node.right)
            if RH == -1:
                return -1

            if abs(LH - RH) > 1:
                return -1

            return 1 + max(LH, RH)

        x = solve(root)

        if x == -1:
            return False

        return True


        
        
