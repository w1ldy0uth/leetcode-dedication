from typing import List


class Solution:
  def predictTheWinner(self, nums: List[int]) -> bool:
    """
    486. Predict the Winner

    Let dp[right] represent the maximum score advantage the current player can obtain from an interval. 
    For each interval, choose the left or right number and subtract the opponent's best resulting advantage. 
    Player 1 wins if the final advantage is nonnegative.

    Time: O(n^2)
    Space: O(n)
    """
    n = len(nums)
    dp = nums[:]

    for left in range(n - 2, -1, -1):
      for right in range(left + 1, n):
        take_left = nums[left] - dp[right]
        take_right = nums[right] - dp[right - 1]
        dp[right] = max(take_left, take_right)

    return dp[-1] >= 0


print(Solution().predictTheWinner([1, 5, 2]))  # False
print(Solution().predictTheWinner([1, 5, 233, 7]))  # True
