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
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list.
        The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list.
        :param list1:
        :param list2:
        :return:
        """
        list3 = ListNode()
        start = list3
        while list1 or list2 :
            if list1 is None and list2:
                list3.next = list2
                list2 = list2.next
            elif list1 and list2 is None:
                list3.next = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    list3.next = list1
                    list1 = list1.next
                elif list1.val > list2.val:
                    list3.next = list2
                    list2 = list2.next
            list3 = list3.next
            list3.next = None

        return start.next


def create_linked_list(input_board: [int]):
    n = len(input_board) - 1
    if n<0:
        return None
    node_last = ListNode(input_board[n], None)
    while n > 0:
        n -= 1
        node_last = ListNode(input_board[n], node_last)
    return node_last


def some_test():
    a = Solution()
    input_board1 = []
    input_board2 = []
    input_list1 = create_linked_list(input_board1)
    input_list2 = create_linked_list(input_board2)

    print(input_list1)
    print(input_list2)
    res = a.mergeTwoLists(input_list1, input_list2)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
