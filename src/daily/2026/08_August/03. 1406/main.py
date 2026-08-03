from typing import List


class Solution:
  def stoneGameIII(self, stoneValue: List[int]) -> str:
    """
    1406. Stone Game III

    Each turn takes 1 to 3 stones, so from index i the current player picks the option
    that maximizes (what they take) -(best the opponent can do afterward).

    Time: O(n)
    Space: O(n)
    """
    n = len(stoneValue)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
      take, best = 0, float('-inf')
      for k in range(1, 4):
        if i + k > n:
          break
        take += stoneValue[i + k - 1]
        best = max(best, take - dp[i + k])
      dp[i] = best

    if dp[0] > 0:
      return "Alice"
    elif dp[0] < 0:
      return "Bob"
    else:
      return "Tie"


print(Solution().stoneGameIII([1, 2, 3, 7]))  # "Bob"
print(Solution().stoneGameIII([1, 2, 3, -9]))  # "Alice"
print(Solution().stoneGameIII([1, 2, 3, 6]))  # "Tie"
