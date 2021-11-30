class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_1, list_2 = [], []

        # traverse linked lists and append results to lists
        node_one, node_two = l1, l2
        while node_one or node_two:
            if node_one:
                list_1.append(node_one.val)
                node_one = node_one.next
            if node_two:
                list_2.append(node_two.val)
                node_two = node_two.next

        # change from [1, 2] to "12"
        x = ''.join(map(str, list_1))
        y = ''.join(map(str, list_2))

        # change from "12" to 21
        xx, yy = int(x[::-1]), int(y[::-1])

        # change to [4, 6]
        result = list(map(int, str(xx + yy)[::-1]))

        # add to node
        head = ListNode()
        tmp = head

        for i, s in enumerate(result):
            if i == 0:
                tmp.val = int(s)
            else:
                x = ListNode(int(s))
                tmp.next = x
                tmp = tmp.next

        return head
