class Node:
    def __init__(self, val=0, neighbors=None, parent=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.parent = parent
        self.size = 1


class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


def some_test():
    a = Solution()
    input_board = [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]
    target = 4
    print(input_board)
    res = a.findRedundantConnection(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
