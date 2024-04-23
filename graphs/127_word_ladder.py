class Node:
    def __init__(self, val="", neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        # self.parent_val = None

    def add_node(self, other):
        self.neighbors.append(other)
        # other.parent_val = self.parent_val

    def is_next(self, other):
        dif = 0
        for i in range(len(self.val)):
            if self.val[i] != other.val[i]:
                dif+=1
        return False if dif != 1 else True

    def __repr__(self):
        s =f"Node( val = {self.val}, neighbors = ["
        if len(self.neighbors)!=0:
            for n in self.neighbors:
                s+=f"{n.val} ,"
            s=s[:-1]
        s+="])"
        return s

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList:
            return 0


def some_test():
    a = Solution()
    wordList = ["most","mist","miss","lost","fist","fish"]
    beginWord = "lost"
    endWord = "miss"
    print(wordList)
    res = a.ladderLength(beginWord, endWord, wordList)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
