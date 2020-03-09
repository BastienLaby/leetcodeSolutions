class Node:
    def __init__(self, l):
        self.l = l
        self.p = -1
        self.parents = {}
        self.encountered = False


class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        """
        First create a hashmap representing the graph node.
        Then, iterate over every node and update the node P parameter if the parent P + distance to parent is less than the current P (or current P note defined).
        At the end of each iteration, if the graph state didn't change, stop the loop.

        Time complexity : ?
        Space complexity : O(N) where N is the number of node.
        """

        nodes = {n: Node(n) for n in range(1, N + 1)}

        for src, dst, t in times:
            nodes[dst].parents[src] = t
        nodes[K].p = 0

        while True:
            graph = {n: nodes[n].p for n in range(1, N + 1)}
            for n, node in nodes.items():
                for parent, dstToParent in node.parents.items():
                    parentNode = nodes[parent]
                    if parentNode.p == -1:
                        continue
                    if node.p == -1 or parentNode.p + dstToParent < node.p:
                        node.p = parentNode.p + dstToParent
            if graph == {n: nodes[n].p for n in range(1, N + 1)}:
                break

        if any(i.p == -1 for i in nodes.values()):
            return -1
        return max([i.p for i in nodes.values()])

