class TrieNode:
    def __init__(self):
        self.is_word = False
        self.char_dict = {}


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
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
        node = self.head
        return self.search_word_continue(word,node)

    def search_word_continue(self, word: str , node:TrieNode):
        """
        call this function if the prev char was '.'
        :param word:
        :param node:
        :return:
        """
        idx = 0
        while idx < len(word):
            char = word[idx]
            if char == "." and len(node.char_dict) != 0:
                res = False
                new_word = "" if idx +1 >= len(word) else word[idx+1:]
                for key in node.char_dict:
                    res = res or self.search_word_continue(new_word,node.char_dict[key])
                    if res:
                        return res
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
    a = WordDictionary()
    a.addWord("apple")
    a.addWord("app")
    a.addWord("application")
    print(a.search("apple"))
    print(a.search("app"))
    print(a.search("applicatioa"))
    print(a.search("applicatio."))
    print(a.search("a.p"))
    print(a.search("..p"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
