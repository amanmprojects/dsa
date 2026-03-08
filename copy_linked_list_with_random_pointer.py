from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodes = []
        head2 = head

        while head2 is not None:
            nodes.append(head2)
            head2 = head2.next

        map = {}

        for n, i in enumerate(nodes):
            map[n] = i

        new_nodes = []

        # create new nodes without next and random pointers
        for n in nodes:
            curr = Node(n.val)
            new_nodes.append(curr)

        new_nodes.append(None)

        # Add next and random pointer 
        for n, i in enumerate(nodes):
            new_nodes[i].next = new_nodes[i+1]

            ran_of_curr = n.random
            if ran_of_curr is None:
                new_nodes[i].random = None
                continue
            ri = map[ran_of_curr]
            new_nodes[i].random = new_nodes[ri]

        return new_nodes[0]


        

        

        