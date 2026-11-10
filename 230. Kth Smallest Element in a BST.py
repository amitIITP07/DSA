class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while curr or stack:

            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit the node
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            # Move to the right subtree
            curr = curr.right
