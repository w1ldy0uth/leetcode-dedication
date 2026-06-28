from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    """
    2130. Maximum Twin Sum of a Linked List

    Collect all values, then pair first half with reversed second half.
    O(n) time, O(n) space.
    """
    vals = []
    node = head
    while node:
      vals.append(node.val)
      node = node.next
    n = len(vals)
    return max(vals[i] + vals[n - 1 - i] for i in range(n // 2))


def make_list(vals):
  dummy = ListNode()
  cur = dummy
  for v in vals:
    cur.next = ListNode(v)
    cur = cur.next
  return dummy.next


print(Solution().pairSum(make_list([5, 4, 2, 1])))   # 6
print(Solution().pairSum(make_list([4, 2, 2, 3])))   # 7
print(Solution().pairSum(make_list([1, 100000])))     # 100001
