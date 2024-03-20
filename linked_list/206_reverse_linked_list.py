# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # lets get the last
        if head is None:
            return head

        node = head

        # self.num = 0

        def requr(node: ListNode):
            if node.next is None:
                return node, node

            # self.num+=1
            # print(f"num = {self.num}")
            head, tail = requr(node.next)
            node.next = None
            tail.next = node
            return head, node

        return requr(node)[0]

    def iterative_answer(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def requirsive_answer(self, head):
        # lets get the last
        node = head

        def requr(node: ListNode):
            if node.next is None:
                return node, node

            head, tail = requr(node.next)
            node.next = None
            tail.next = node
            return head, node

        return requr(node)[0]


def some_test():
    a = Solution()
    input_board = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(input_board) - 1
    node_last = ListNode(input_board[n], None)
    while n > 0:
        n -= 1
        node_last = ListNode(input_board[n], node_last)
    print(input_board)
    res = a.iterative_answer(node_last)

    print(res.val)
    while res.next is not None:
        print(res.next.val)
        res = res.next

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
