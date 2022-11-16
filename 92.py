# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        prev, cur = None, head

        for _ in range(left - 1):
            prev, cur = cur, cur.next
        
        connector_node, new_tail = prev, cur

        for _ in range(left - 1, right):
            next = cur.next

            cur.next = prev

            prev = cur
            cur = next
        
        new_tail.next = next

        if connector_node:
            connector_node.next = prev
        else:
            head = prev

        return head
