# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # edge case
        if head.next == None:
            return

        # general case
        d = {}
        pos, cur = 0, head
        while cur != None:
            d[pos] = cur
            pos, cur = pos+1, cur.next
            
        i, j = 0, len(d)-1
        sentinel = ListNode(-1)
        cur = sentinel
        while i <= j:
            if i <= j:
                cur.next = d[i]
                i += 1
                cur = cur.next
            if i < j:
                cur.next = d[j]
                j -= 1
                cur = cur.next
        cur.next = None