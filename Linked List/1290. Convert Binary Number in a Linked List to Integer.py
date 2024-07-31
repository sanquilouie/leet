class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize result to 0
        result = 0

        # Traverse the linked list
        current = head
        while current:
            # Shift result left by 1 (binary multiplication by 2) and add the current node's value
            result = (result << 1) | current.val
            # Move to the next node
            current = current.next

        return result
