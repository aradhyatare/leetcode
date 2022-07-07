
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        v = {}
        def clone(node):
            if not node: return None
            if node not in v:
                cloneNode = Node(node.val)
                v[node] = cloneNode
                cloneNode.neighbors = [clone(n) for n in node.neighbors]
            return v[node]
        return clone(node)