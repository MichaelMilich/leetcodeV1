class Node:
    def __init__(self, val=0, prerequisites=None):
        self.val = val
        self.prerequisites = prerequisites if prerequisites is not None else []

    def __repr__(self):
        s = f"Node(val ={self.val} , prerequisites =["
        if self.prerequisites:
            for pre in self.prerequisites:
                s += f" {pre.val} ,"
            s = s[:-1]
        s += "] )"
        return s


class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        courses = {idx: Node(val=idx) for idx in range(numCourses)}
        for pre in prerequisites:
            courses[pre[0]].prerequisites.append(courses[pre[1]])
        q = []
        visited = set()
        ok = set()

        def dfs(node : Node):
            if not node.prerequisites:
                ok.add(node)
                return True
            if node in visited:
                return False
            res= True
            visited.add(node)
            for pre in node.prerequisites:
                if pre not in ok:
                    res = res and dfs(pre)
            if res:
                ok.add(node)
            return res

        for node in courses.values():
            visited=set()
            res = dfs(node)
            if not res:
                return False

        return True


def some_test():
    a = Solution()
    input_board = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
    target = 8
    print(input_board)
    res = a.canFinish(target, input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
