# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head

        for _ in range(left - 1):
            prev = cur
            cur = cur.next
        
        left_prev = prev
        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next

