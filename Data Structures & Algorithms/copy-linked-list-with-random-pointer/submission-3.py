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
        
        old_to_new_map = defaultdict(lambda: Node(0))
        old_to_new_map[None] = None

        cur = head
        while cur:
            old_to_new_map[cur].val = cur.val
            old_to_new_map[cur].next = old_to_new_map[cur.next]
            old_to_new_map[cur].random = old_to_new_map[cur.random]
            
            cur = cur.next
 
        return old_to_new_map[head]





        
