#Here is an example solution in Python to remove the nth node from the end of a linked list and return its head:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Advance first pointer n+1 steps from the beginning
        for i in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        # Skip the desired node
        second.next = second.next.next

        return dummy.next

'''
In this solution, two pointers first and second are used to maintain a gap of n nodes between them. 
The first pointer is advanced n + 1 steps 
from the beginning, and then both pointers are moved together until 
first reaches the end. The second.next node is then skipped, effectively removing the nth node from the end of the linked list.
'''