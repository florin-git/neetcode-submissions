"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # store the new created nodes in an hash_map
        # for every neighbor in a node create the link between the new created nodes

        if not node:
            return None
            
        new_nodes = {}
        new_nodes[node.val] = Node(node.val)

        queue = deque()
        queue.append(node)

        while queue:
            n = queue.popleft()
            
            for nei in n.neighbors:

                if nei.val in new_nodes:
                    new_nei = new_nodes[nei.val]
                else:
                    new_nei = Node(val=nei.val)
                    new_nodes[nei.val] = new_nei
                    queue.append(nei)

                new_nodes[n.val].neighbors.append(new_nei)

        return new_nodes[1]








