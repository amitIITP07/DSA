class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and last node
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        # Step 2: Reduce unnecessary rotations
        k = k % n

        if k == 0:
            return head

        # Step 3: Make the list circular
        tail.next = head

        # Step 4: Find the new last node
        steps = n - k
        new_tail = head

        for i in range(steps - 1):
            new_tail = new_tail.next

        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
