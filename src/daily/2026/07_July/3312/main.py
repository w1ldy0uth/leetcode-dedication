import bisect
from typing import List


class Solution:
  def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
    """
    3312. Sorted GCD Pair Queries

    Count how many pairs have GCD exactly equal to each value g,
    using a divisor-counting trick (similar to Möbius/sieve techniques)

    Time: O(m log m + Q log m)
    Space: O(m)
    """
    maxV = max(nums)
    freq = [0] * (maxV + 1)
    for x in nums:
      freq[x] += 1

    m = [0] * (maxV + 1)
    for g in range(1, maxV + 1):
      s = 0
      for k in range(g, maxV + 1, g):
        s += freq[k]
      m[g] = s

    pairs = [0] * (maxV + 1)
    for g in range(1, maxV + 1):
      c = m[g]
      pairs[g] = c * (c - 1) // 2

    exact = [0] * (maxV + 1)
    for g in range(maxV, 0, -1):
      s = pairs[g]
      for k in range(2 * g, maxV + 1, g):
        s -= exact[k]
      exact[g] = s

    gs = []
    prefix = []
    total = 0
    for g in range(1, maxV + 1):
      if exact[g] > 0:
        total += exact[g]
        gs.append(g)
        prefix.append(total)

    ans = []
    for q in queries:
      idx = bisect.bisect_right(prefix, q)
      ans.append(gs[idx])
    return ans
