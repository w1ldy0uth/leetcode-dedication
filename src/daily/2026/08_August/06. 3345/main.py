import math


class Solution:
  def smallestNumber(self, n: int, t: int) -> int:
    """
    3345. Smallest Divisible Digit Product I

    Assuming that we need to look up to at most 10 numbers, simply check them
    in order and return the first one that satisfies the condition.

    Time: O(1)
    Space: O(1)
    """
    def n_prod(x): return math.prod(int(d) for d in str(x))

    for i in range(11):
      if (n_prod(n + i)) % t == 0:
        return n + i


print(Solution().smallestNumber(10, 2))  # 10
print(Solution().smallestNumber(15, 3))  # 16
