from typing import List, Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    25. Reverse Nodes in k-Group

    Reverse every k nodes in the list, leaving the last group as is if it has
    fewer than k nodes.

    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
      kth = group_prev
      for _ in range(k):
        kth = kth.next
        if not kth:
          return dummy.next

      group_next = kth.next
      prev, curr = group_prev.next, group_prev.next.next
      for _ in range(k - 1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

      tail = group_prev.next
      tail.next = group_next
      group_prev.next = prev

      group_prev = tail


def to_list(node):
  result = []
  while node:
    result.append(node.val)
    node = node.next
  return result


print(to_list(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)))  # Output: [2,1,4,3,5]
print(to_list(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)))  # Output: [3,2,1,4,5]
