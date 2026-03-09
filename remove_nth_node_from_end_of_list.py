from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head2 = head
        count = 0
        while head2 is not None:
            count += 1
            head2 = head2.next

        if count == 1:
            return head

        target = count - n - 1

        if target < 0:
            head = head.next
            return head

        for i in range(target):
            head = head.next
        
        head.next = head.next.next
        