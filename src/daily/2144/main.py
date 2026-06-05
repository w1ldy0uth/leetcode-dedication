from typing import List


class Solution:
  def minimumCost(self, cost: List[int]) -> int:
    """
    2144. Minimum Cost of Buying Candies With Discount

    Sort descending and skip every third candy — the free candy is always
    the cheapest in its group of three, which maximizes the discount taken.
    """
    return sum(c for i, c in enumerate(sorted(cost, reverse=True)) if (i + 1) % 3 != 0)


print(Solution().minimumCost([1, 2, 3]))           # 5
print(Solution().minimumCost([6, 5, 7, 9, 2, 2]))  # 23
print(Solution().minimumCost([5, 5]))               # 10
