from typing import List


class Solution:
  def maxIceCream(self, costs: List[int], coins: int) -> int:
    """
    1833. Maximum Ice Cream Bars

    Greedy: buy cheapest bars first. Use counting sort (costs[i] <= 10^5)
    to bucket prices, then sweep from cheapest, buying as many as budget allows.

    Time: O(n + m) where m = max(costs).
    Space: O(m).
    """
    m = max(costs)
    count = [0] * (m + 1)
    for c in costs:
      count[c] += 1

    bought = 0
    for price in range(1, m + 1):
      if count[price] == 0:
        continue
      can = min(count[price], coins // price)
      bought += can
      coins -= can * price
      if coins <= 0:
        break
    return bought


print(Solution().maxIceCream([1, 3, 2, 4, 1], 7))       # 4
print(Solution().maxIceCream([10, 6, 8, 7, 7, 8], 5))   # 0
print(Solution().maxIceCream([1, 6, 3, 1, 2, 5], 20))   # 6
