from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # Array to store the nodes in sorted order
        sorted_nodes = []

        # Appending the nodes to sorted array
        while lists:
            min_node = ListNode(val=1001)
            min_index = -1
            # Find the minimum node and its index
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < min_node.val:
                    min_node = lists[i]
                    min_index = i
            if min_index == -1:
                # All lists are empty
                break
            # Append the minimum node
            sorted_nodes.append(min_node)
            # Advance the corresponding list
            lists[min_index] = lists[min_index].next
            # Remove lists that are now None
            lists = [l for l in lists if l is not None]

        # Add the Link
        if not sorted_nodes:
            return None
        for i in range(len(sorted_nodes)-1):
            sorted_nodes[i].next = sorted_nodes[i+1]
        sorted_nodes[-1].next = None
        return sorted_nodes[0]


                
                

        