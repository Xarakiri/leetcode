# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #       None -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
        # cur     |                 
        # result  |
        cur = ListNode(0)
        cur.next = head

        result = cur
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return result.next
