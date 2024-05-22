import string
import heapq


class Node:
    char_val_dict = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}

    def __init__(self, val="", neighbors=None):
        self.val = val
        self.h_val = self.string_to_h_val(val)
        self.neighbors = neighbors if neighbors is not None else []
        # self.parent_val = None

    def add_node(self, other):
        self.neighbors.append(other)
        # other.parent_val = self.parent_val

    def is_next(self, other):
        dif = 0
        for i in range(len(self.val)):
            if self.val[i] != other.val[i]:
                dif += 1
        return False if dif != 1 else True

    def __repr__(self):
        s = f"Node( val = {self.val}, h_val ={self.h_val}, neighbors = ["
        if len(self.neighbors) != 0:
            for n_val, n in self.neighbors:
                s += f"{n.val} ,"
            s = s[:-1]
        s += "])"
        return s

    def __le__(self, other):
        return self.h_val < other.h_val

    def __lt__(self, other):
        return self.h_val <= other.h_val

    @staticmethod
    def string_to_h_val(s: str):
        h_val = 0
        for i in range(len(s)):
            h_val += Node.char_val_dict[s[i]] * 26 ** i
        return h_val


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList:
            return 0
        # create the graph
        wordList.insert(0, beginWord)
        node_dict = {}
        # start by creating all the nodes
        for word in wordList:
            node_dict[word] = Node(word)

        target = node_dict[endWord].h_val
        # connect all the nodes to its neighbors
        for word, val in node_dict.items():
            for word2, val2 in node_dict.items():
                if word == word2:
                    continue
                if val.is_next(val2):
                    if (abs(val2.h_val - target), val2) not in val.neighbors:
                        heapq.heappush(val.neighbors, (abs(val2.h_val - target), val2))
                    if (abs(val.h_val - target), val) not in val2.neighbors:
                        heapq.heappush(val2.neighbors, (abs(val.h_val - target), val))
        # start a star algorithm

        node = node_dict[beginWord]
        visited = {node}
        path_taken = 0
        best_path_q = []
        heapq.heappush(best_path_q, (node.h_val, node, path_taken + 1))
        while best_path_q:
            node_h_val, node, nodes_path_num = heapq.heappop(best_path_q)
            while node.neighbors:
                node_f_h, next_node = heapq.heappop(node.neighbors)
                if next_node.val == endWord:
                    return nodes_path_num + 1
                if next_node not in visited:
                    heapq.heappush(best_path_q, (node_f_h, next_node, nodes_path_num + 1))
                visited.add(next_node)
        return 0


def some_test():
    a = Solution()
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
                "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge",
                "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh",
                "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be",
                "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
    beginWord = "qa"
    endWord = "sq"
    print(wordList)
    res = a.ladderLength(beginWord, endWord, wordList)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
