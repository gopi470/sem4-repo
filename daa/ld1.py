class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


def merge_k_lists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            merged.append(merge_two(l1, l2))

        lists = merged

    return lists[0]


def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)


lists = [
    build_list([1,4,5]),
    build_list([1,3,4]),
    build_list([2,6])
]

result = merge_k_lists(lists)
print_list(result)
