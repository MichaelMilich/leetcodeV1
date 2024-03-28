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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = new_node = ListNode()
        sum_trail = 0
        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            sum_temp = (val1 + val2 + sum_trail) % 10
            new_node.val = sum_temp
            sum_trail = (val1 + val2 + sum_trail) // 10
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
            if l1 or l2:
                new_node.next = ListNode()
                new_node = new_node.next
            elif sum_trail != 0:
                new_node.next = ListNode(val=sum_trail)
        return new_head


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
    input_board1 = [9, 9, 9, 9, 9, 9, 9]
    input_board2 = [9, 9, 9, 9]
    input_list1 = create_linked_list(input_board1)
    input_list2 = create_linked_list(input_board2)

    print(input_list1)
    res = a.addTwoNumbers(input_list1, input_list2)
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()


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
    input_board1 = [9, 9, 9, 9, 9, 9, 9]
    input_board2 = [9, 9, 9, 9]
    input_list1 = create_linked_list(input_board1)
    input_list2 = create_linked_list(input_board2)

    print(input_list1)
    res = a.addTwoNumbers(input_list1, input_list2)
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()