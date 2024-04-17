from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_dict = {}
        head = node
        q = [node]
        while q:
            node = q.pop()
            if node not in node_dict:
                node_dict[node] = Node(node.val)
                if node.neighbors is not None:
                    q.extend(node.neighbors)

        for key, val in node_dict.items():
            for node in key.neighbors:
                val.neighbors.append(node_dict[node])

        return node_dict[head]
