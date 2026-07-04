from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    24. Swap Nodes in Pairs

    Swap every two adjacent nodes in the linked list.

    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
      first = prev.next
      second = first.next
      first.next = second.next
      second.next = first
      prev.next = second
      prev = first

    return dummy.next


def to_list(node):
  result = []
  while node:
    result.append(node.val)
    node = node.next
  return result


print(to_list(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))))  # Output: [2,1,4,3]
print(to_list(Solution().swapPairs(ListNode(1))))  # Output: [1]
print(to_list(Solution().swapPairs(None)))  # Output: []
print(to_list(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3))))))  # Output: [2,1,3]
