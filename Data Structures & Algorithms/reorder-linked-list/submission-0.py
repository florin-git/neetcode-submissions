# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse_head = self.reverse_list(slow.next)
        slow.next = None

        first = head
        second = reverse_head

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

    

    def reverse_list(self, head) -> ListNode:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

