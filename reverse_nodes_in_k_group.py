from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []
        curr = head

        while curr is not None:
            rev = []
            for i in range(k):
                if curr == None:
                    return self.listToLinkedList(res + rev)
                rev.append(curr)
                curr = curr.next
            rev.reverse()
            res += rev
        return self.listToLinkedList(res)

    def listToLinkedList(self, l: List[ListNode]) -> Optional[ListNode]:
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]
    

            