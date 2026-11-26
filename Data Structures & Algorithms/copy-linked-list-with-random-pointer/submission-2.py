"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_to_new_map = {None: None}
        cur = head  

        # initialize new nodes
        while cur:
            new_node = Node(cur.val)
            old_to_new_map[cur] = new_node
            cur = cur.next

        # link nodes
        cur = head
        while cur:
            new_node = old_to_new_map[cur]

            new_next = old_to_new_map[cur.next]
            new_node.next = new_next
            
            new_random = old_to_new_map[cur.random]
            new_node.random = new_random

            cur = cur.next

            
        return old_to_new_map[head]





        
