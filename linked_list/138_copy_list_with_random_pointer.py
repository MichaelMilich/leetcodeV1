class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        if self.next is None:
            return f"Node [ val = {self.val} , random = ({self.random}), next = None]"
        else:
            return f"Node[ val = {self.val} , random = ({self.random}) ] => \n {self.next}"

    def __repr__(self):
        if self.next is None:
            return f"Node [ val = {self.val}, random = ({self.random}) , next = None]"
        else:
            return f"Node[ val = {self.val} , random = ({self.random})] next = {self.next}"


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        node_dict = {}
        temp = head
        while head:
            node_dict[head] = Node(head.val)
            head=head.next
        for key,val in node_dict.items():
            if key.next:
                val.next = node_dict[key.next]
            if key.random:
                val.random = node_dict[key.random]
        return node_dict[temp]

def create_linked_list(input_board: []):
    n = len(input_board) - 1
    if n < 0:
        return None
    list_dict = {}
    for index, element in enumerate(input_board):
        list_dict[index] = Node(element[0], None, element[1])
    for key in list_dict:
        if key + 1 in list_dict:
            list_dict[key].next = list_dict[key + 1]
    return list_dict[0]


def some_test():
    a = Solution()
    input_board1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    target = 1
    input_list1 = create_linked_list(input_board1)

    print(input_list1)
    res = a.copyRandomList(input_list1)
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
