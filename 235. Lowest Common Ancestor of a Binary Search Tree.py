class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root 
        while True:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            elif p.val > curr.val and q.val > curr.val :
                curr = curr.right
            elif p == curr:
                return p
            elif q == curr:
                return q
            else:
                return curr
