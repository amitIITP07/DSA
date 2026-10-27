class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        length = 0

        # Step 1: Count the nodes
        while temp is not None:
            length += 1
            temp = temp.next

        # Step 2: Handle removal of the first node
        if length == n:
            return head.next

        # Step 3: Reach the node before the one to remove
        temp = head
        for i in range(length - n - 1):
            temp = temp.next

        # Step 4: Remove the node
        temp.next = temp.next.next

        return head
