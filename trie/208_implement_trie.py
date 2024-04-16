class TrieNode:
    def __init__(self):
        self.is_word = False
        self.char_dict = {}


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        idx = 0
        node = self.head
        while idx < len(word):
            char = word[idx]
            if char not in node.char_dict:
                node.char_dict[char] = TrieNode()
            node = node.char_dict[char]
            idx += 1
        node.is_word = True

    def search(self, word: str) -> bool:
        idx = 0
        node = self.head
        while idx < len(word):
            char = word[idx]
            if char not in node.char_dict:
                return False
            node = node.char_dict[char]
            idx += 1
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        idx = 0
        node = self.head
        while idx < len(prefix):
            char = prefix[idx]
            if char not in node.char_dict:
                return False
            node = node.char_dict[char]
            idx += 1
        return self.search_word_end(node)

    def search_word_end(self, node: TrieNode):
        if node.is_word:
            return True
        if len(node.char_dict) == 0:
            return False
        res = False
        for char in node.char_dict:
            res = res or self.search_word_end(node.char_dict[char])
            if res:
                return True
        return res


def some_test():
    a = Trie()
    a.insert("apple")
    a.insert("app")
    a.insert("application")
    print(a.search("apple"))
    print(a.search("app"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
