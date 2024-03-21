# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return f"ListNode [ val = {self.val}, next = None]"
        else:
            return f"ListNode[ val = {self.val} ] => \n {self.next}"

    def __repr__(self):
        if self.next is None:
            return f"ListNode [ val = {self.val}, next = None]"
        else:
            return f"ListNode[ val = {self.val} ] next = {self.next}"


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        todo: do this question with memory of O(1) instead of O(n) . keep time complexity at O(n)
        """
        if not head:
            return

        node_index = 0
        node_dict = dict()
        start = head
        while head:
            temp = head
            head = head.next
            temp.next = None
            node_dict[node_index] = temp
            node_index += 1
        node_index -= 1
        head = start
        i = 1
        while i < node_index:
            head.next = node_dict[node_index]
            node_index -= 1
            head = head.next
            head.next = node_dict[i]
            i += 1
            head = head.next
        print(f"i = {i}, node_index = {node_index}")
        if i == node_index:
            head.next = node_dict[i]


def create_linked_list(input_board: [int]):
    n = len(input_board) - 1
    if n < 0:
        return None
    node_last = ListNode(input_board[n], None)
    while n > 0:
        n -= 1
        node_last = ListNode(input_board[n], node_last)
    return node_last


def some_test():
    a = Solution()
    input_board1 = [1, 2]
    input_list1 = create_linked_list(input_board1)

    print(input_list1)
    a.reorderList(input_list1)
    print(input_list1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
