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

        queue = deque()
        queue.append(node)
        visited = set()

        while queue:
            n = queue.popleft()

            if n in visited:
                continue

            visited.add(n)

            # create copy
            # check if it was already created
            if n.val in new_nodes:
                new_n = new_nodes[n.val]
            else:
                new_n = Node(val=n.val)
                new_nodes[n.val] = new_n

            
            for nei in n.neighbors:

                if nei.val in new_nodes:
                    new_nei = new_nodes[nei.val]
                else:
                    new_nei = Node(val=nei.val)
                    new_nodes[nei.val] = new_nei

                # is this called multiple times over the same new node
                new_n.neighbors.append(new_nei)

                if nei not in visited:
                    queue.append(nei)


        return new_nodes[1]










