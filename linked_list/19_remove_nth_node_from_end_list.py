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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        dummy = ListNode(0, head)
        left, right = dummy, head
        size = 1
        while size < n and right:
            right = right.next
            size += 1

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

    def removeWithDict(self, head: ListNode, n: int) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        todo: do this question with memory of O(1) instead of O(n) . keep time complexity at O(n)
        """
        if not head:
            return

        node_index = 0
        node_dict = dict()
        while head:
            temp = head
            head = head.next
            node_dict[node_index] = temp
            node_index += 1

        node_index -= n
        if node_index - 1 in node_dict:
            if node_index + 1 in node_dict:
                node_dict[node_index - 1].next = node_dict[node_index + 1]
            else:
                node_dict[node_index - 1].next = None
        else:
            if node_index + 1 in node_dict:
                return node_dict[node_index + 1]
            else:
                return None
        return node_dict[0]


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
    input_board1 = [1,2]
    target = 1
    input_list1 = create_linked_list(input_board1)

    print(input_list1)
    res = a.removeNthFromEnd(input_list1, target)
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
