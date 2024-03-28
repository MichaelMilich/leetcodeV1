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
    def hasCycle(self, head: ListNode) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        :param head:
        :return:
        """
        if not head:
            return False
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False



    def hasCycleSet(self, head: ListNode) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        :param head:
        :return:
        """
        dummy = head
        node_set = {head}
        while dummy:
            dummy= dummy.next
            if dummy in node_set:
                return True
            else:
                node_set.add(dummy)
        return False



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