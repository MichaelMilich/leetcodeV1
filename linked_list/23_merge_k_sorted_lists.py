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
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        """
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.
        :param lists:
        :return:
        """
        corrected_list = []
        for node in lists:
            if node is not None:
                corrected_list.append(node)
        if not corrected_list:
            return None

        stack = sorted(corrected_list, key=lambda x: x.val)
        head = temp = node = stack[0]
        temp = temp.next
        stack.pop(0)
        print(f" stack = {list(map(lambda x: x.val, stack))}")
        if temp is not None:
            stack = self.inset_to_sorted_stack(stack,temp)
        while stack:
            print(f" stack = {list(map(lambda x: x.val, stack))}")
            node.next = stack[0]
            node = temp = stack.pop(0)
            temp = temp.next
            if temp is not None:
                stack = self.inset_to_sorted_stack(stack, temp)

        return head

    def inset_to_sorted_stack(self, stack: [ListNode], node: ListNode):
        if not stack:
            stack.append(node)
            return stack
        if node.val < stack[0].val:
            stack.addWord(0)
            return stack
        if node.val >= stack[-1].val:
            stack.append(node)
            return stack

        n = len(stack)
        l, r = 0, n - 1
        mid = (r - l) // 2 +l
        while l < r:
            mid = (r - l) // 2 +l
            if node.val == stack[mid].val:
                break
            elif node.val > stack[mid].val:
                l = mid + 1
            elif node.val < stack[mid].val:
                r = mid - 1
        if node.val <= stack[l].val:
            stack.addWord(l)
        elif node.val <= stack[mid].val:
            stack.addWord(mid)
        else:
            while node.val > stack[mid].val:
                mid = mid+1
            stack.addWord(mid)
        print(f" stack = {list(map(lambda x: x.val, stack))}")
        return stack


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
    input_lists = [[-3,2,2],[-9],[-10,-5,-4,-2,-1,1,3,4],[-10,-9,-8,3,4],[-5,-3,3,4],[-9,-8,-5,-4,-2,-1,3]]
    input_lists = list(map(lambda x: create_linked_list(x), input_lists))

    for i in range(len(input_lists)):
        print(f"{i}: {input_lists[i]}")
    res = a.mergeKLists(input_lists)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
