# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    19. Remove Nth Node From End of List
    
    Using two pointers, move the fast pointer n steps ahead of the slow pointer.
    After fast pointer reaches the end, the slow pointer will be at the node before the one to remove.
    
    Time: O(n) — traverse the list once.
    Space: O(1)
    """
    tmp = ListNode(0, head)
    slow = fast = tmp

    for _ in range(n + 1):
      fast = fast.next

    while fast:
      fast = fast.next
      slow = slow.next

    slow.next = slow.next.next
    return tmp.next


print(Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2).val)  # [1,2,3,5]
print(Solution().removeNthFromEnd(ListNode(1), 1))  # []
print(Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 1).val)  # [1]
