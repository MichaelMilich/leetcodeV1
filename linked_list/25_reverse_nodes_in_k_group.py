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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

        k is a positive integer and is less than or equal to the length of the linked list.
        If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
        You may not alter the values in the list's nodes, only nodes themselves may be changed.

        Constraints:
            The number of nodes in the list is n.
            1 <= k <= n <= 5000
            0 <= Node.val <= 1000

        :param head:
        :param k:
        :return:
        """
        dummy = ListNode(val=0, next=head)
        prev = dummy
        num = 1
        stack = [head]
        while head:
            head = head.next
            if head:
                num += 1
                stack.append(head)
            if num == k:
                next_node= None if head is None else head.next
                temp = stack.pop()
                temp.next = None
                prev.next = temp
                while stack:
                    temp2 = stack.pop()
                    temp2.next = None
                    temp.next = temp2
                    temp = temp2
                prev = temp
                num = 1
                head = next_node
                stack = [head]
        while stack:
            prev.next = stack.pop(0)
            prev = prev.next

        return dummy.next


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
    input_lists = [[ 3]]
    target = 1
    input_lists = list(map(lambda x: create_linked_list(x), input_lists))

    for i in range(len(input_lists)):
        print(f"{i}: {input_lists[i]}")
    res = a.reverseKGroup(input_lists[0], target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
