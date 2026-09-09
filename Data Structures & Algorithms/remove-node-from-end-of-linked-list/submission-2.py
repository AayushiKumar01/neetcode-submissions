# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        nodes = []

        temp = head
        while head:
            nodes.append(head)
            head = head.next

        if len(nodes) == 1:
            return None

        # j = len(nodes) - 1

        # while n:
        #     j -= 1
        #     n -= 1

        j = len(nodes)-1 - n

        if j == -1 and len(nodes) > 1:
            return nodes[1]
        nodes[j].next = nodes[j+1].next
        return temp