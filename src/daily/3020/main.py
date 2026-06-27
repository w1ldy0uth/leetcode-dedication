from typing import List


class Solution:
  def maximumLength(self, nums: List[int]) -> int:
    """
    3020. Find the Maximum Number of Elements in Subset
    
    Count frequencies of each number. For x = 1 (as we can use sequence of all 1s) take count rounded to the nearest odd number.
    For each other x, we walk the sequence x, x^2, x^4, ... checking each number's frequency >= 2 (except for the center which needs frequency >= 1).
    Total subset length is 2 * steps + 1.
    
    Time: O(n log log m), where m - max value
    Space: O(n)
    """
    from collections import Counter

    count = Counter(nums)
    res = 1

    for x in count:
      if x == 1:
        c = count[1]
        res = max(res, c if c % 2 == 1 else c - 1)
        continue

      length = 0
      cur = x
      while cur in count and count[cur] >= 2:
        length += 2
        cur *= cur
      if cur in count:
        length += 1
      else:
        length -= 1
      res = max(res, length)

    return res


print(Solution().maximumLength([5, 4, 1, 2, 2]))  # 3
print(Solution().maximumLength([1, 3, 2, 4]))  # 1
