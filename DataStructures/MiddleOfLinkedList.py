#Given the head of a singly linked list, return the middle node of the linked list.
from Cython.Compiler.ExprNodes import ListNode

#If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_list = 0
        start = node = head

        while start:
            len_list += 1
            start = start.next
        middle = len_list // 2
        counter = 0
        while node:
            if counter == middle:
                return node
            else:
                counter += 1
                node = node.next
        return None