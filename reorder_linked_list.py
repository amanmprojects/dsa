from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        head2 = head
        while head2 is not None:
            nodes.append(head2)
            head2 = head2.next
        
        # Reordering
        new_nodes=[]
        i, j = 0, len(nodes)-1

        while len(new_nodes) < len(nodes):
            new_nodes.append(nodes[i])
            new_nodes.append(nodes[j])
            i += 1
            j -= 1

        if len(new_nodes) > len(nodes): new_nodes.pop()

        # Fixing pointers
        for i in range(len(new_nodes)-1):
            new_nodes[i].next = new_nodes[i+1]

        new_nodes[len(new_nodes)-1].next = None

