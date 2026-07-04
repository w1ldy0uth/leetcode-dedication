from typing import List, Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    23. Merge k Sorted Lists

    Push the head of every list into a min-heap keyed by value, then repeatedly
    pop the smallest node, append it to the result, and push its successor.

    Time: O(n log k) — n total nodes, heap of size k.
    Space: O(k) for the heap.
    """
    import heapq

    heap = []
    for i, node in enumerate(lists):
      if node:
        heapq.heappush(heap, (node.val, i, node))

    dummy = tail = ListNode()
    while heap:
      _, i, node = heapq.heappop(heap)
      tail.next = node
      tail = tail.next
      if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


def to_list(node):
  result = []
  while node:
    result.append(node.val)
    node = node.next
  return result


print(to_list(Solution().mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(
    1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])))  # Output: [1,1,2,3,4,4,5,6]
print(to_list(Solution().mergeKLists([])))  # Output: []
print(to_list(Solution().mergeKLists([[]])))  # Output: []
