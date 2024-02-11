# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        if not head.next:
            return head

        p1 = head
        p2 = head.next
        head.next = None

        while p2:
            next_node = p2.next
            p2.next = p1
            p1 = p2
            p2 = next_node

        return p1
    