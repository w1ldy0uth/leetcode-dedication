from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    2095. Delete the Middle Node of a Linked List

    One-pass traversal using fast and slow pointers (after the loop, slow is at the middle).
    O(n) time, O(1) space.
    """
    if head.next is None or head is None:
      return None
    
    prev = None
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
      fast = fast.next.next
      prev = slow
      slow = slow.next
    
    prev.next = slow.next
    
    return head


def make_list(vals):
  dummy = ListNode()
  cur = dummy
  for v in vals:
    cur.next = ListNode(v)
    cur = cur.next
  return dummy.next

print(Solution().deleteMiddle(make_list([1,3,4,7,1,2,6]))) # [1,3,4,1,2,6]
print(Solution().deleteMiddle(make_list([1,2,3,4]))) # [1,2,4]
print(Solution().deleteMiddle(make_list([2,1]))) # [2]