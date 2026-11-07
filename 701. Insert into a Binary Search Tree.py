class Solution(object):
    def insertIntoBST(self, root, val):

        if root is None:
            return TreeNode(val)

        temp = root

        while True:

            if val < temp.val:

                if temp.left is None:
                    temp.left = TreeNode(val)
                    break

                temp = temp.left

            else:

                if temp.right is None:
                    temp.right = TreeNode(val)
                    break

                temp = temp.right

        return root
