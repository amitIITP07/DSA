class Solution:
    def inorderTraversal(self, root):

        result = []
        current = root

        while current is not None:

            # Case 1: Current has no left child
            if current.left is None:
                result.append(current.val)
                current = current.right

            else:
                # Case 2: Current has left child
                # Find the inorder predecessor
                predecessor = current.left

                # Go to the rightmost node in left subtree
                while (predecessor.right is not None and
                       predecessor.right != current):

                    predecessor = predecessor.right

                # Make current as right child of predecessor
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left

                else:
                    # Revert the changes
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result
